from __future__ import unicode_literals
import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from . import managers
from . import fields


class MetaMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class VotingTopic(MetaMixin, models.Model):

    VIEW_PAGE_CHOICES = ((1, "Allow List View"), (2, "Allow Card View"))

    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True)
    submission_information = models.TextField(
        blank=True, null=True,
        help_text="Information to provide to Choice submitters.")

    list_page_view = fields.MultiSelectField(
        default=[x[0] for x in VIEW_PAGE_CHOICES],
        max_length=250, blank=True, choices=VIEW_PAGE_CHOICES)
    list_page_voting = models.BooleanField(
        "Allow voting on the list page.",
        default=False)
    anonymous_voting = models.BooleanField(
        "Allow anonymous voting",
        default=False)
    voting_enabled_date = models.DateTimeField(
        default=datetime.datetime.now, blank=True)
    require_approval = models.BooleanField(
        "Vote Choice Submission Requires Approval", default=True)

    vote_headers = fields.VoteHeaderField(blank=True, null=True)

    objects = managers.VotingTopicQuerySet.as_manager()

    def __str__(self):
        return "{title}".format(title=self.title)

    class Meta:
        verbose_name = "Voting Topic"
        verbose_name_plural = "Voting Topics"

    def get_absolute_url(self):
        return reverse('topics:topic_view', args=[str(self.slug)])

    def choices(self):
        kwargs = {}
        if self.require_approval:
            kwargs['approved'] = True
        return self.votechoice_set.filter(**kwargs)

    def votes(self):
        return Vote.objects.filter(choice__topic=self)

    def enable_list_view(self):
        return True if u'1' in self.list_page_view else False

    def enable_card_view(self):
        return True if u'2' in self.list_page_view else False


@python_2_unicode_compatible
class VoteChoice(MetaMixin, models.Model):
    topic = models.ForeignKey(VotingTopic)
    approved = models.BooleanField("Approved?", default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    text = models.CharField(max_length=255)

    picture = models.ImageField(blank=True, null=True, upload_to="votechoices")
    description = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    link_text = models.CharField(max_length=64, blank=True, null=True)

    def get_link_text(self):
        return self.link_text if self.link_text else self.link

    def __str__(self):
        return "{topic}: {text}".format(topic=self.topic, text=self.text)

    class Meta:
        verbose_name = "Voting Choice"
        verbose_name_plural = "Voting Choices"


@python_2_unicode_compatible
class Vote(MetaMixin, models.Model):
    choice = models.ForeignKey(VoteChoice)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    vote = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "{choice}".format(choice=self.choice)

    class Meta:
        verbose_name = "Vote"
        verbose_name_plural = "Votes"
