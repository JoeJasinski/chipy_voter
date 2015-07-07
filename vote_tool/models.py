import datetime
from django.db import models
from django import forms
from django.utils.text import capfirst
from django.core import exceptions
from django.conf import settings


class MultiSelectFormField(forms.MultipleChoiceField):
    widget = forms.CheckboxSelectMultiple

    def __init__(self, *args, **kwargs):
        self.max_choices = kwargs.pop('max_choices', 0)
        super(MultiSelectFormField, self).__init__(*args, **kwargs)

    def clean(self, value):
        if not value and self.required:
            raise forms.ValidationError(self.error_messages['required'])
        return value


class MultiSelectField(models.Field):
    __metaclass__ = models.SubfieldBase

    def get_internal_type(self):
        return "CharField"

    def get_choices_default(self):
        return self.get_choices(include_blank=False)

    def formfield(self, **kwargs):
        # don't call super, as that overrides default widget if it has choices
        defaults = {
            'required': not self.blank,
            'label': capfirst(self.verbose_name),
            'help_text': self.help_text,
            'choices': self.choices}
        if self.has_default():
            defaults['initial'] = self.get_default()
        defaults.update(kwargs)
        return MultiSelectFormField(**defaults)

    def get_prep_value(self, value):
        return value

    def get_db_prep_value(self, value, connection=None, prepared=False):
        if isinstance(value, basestring):
            return value
        elif isinstance(value, list):
            return ",".join(value)

    def to_python(self, value):
        if value is not None:
            return value if isinstance(value, list) else value.split(',')
        return ''

    def contribute_to_class(self, cls, name):
        super(MultiSelectField, self).contribute_to_class(cls, name)
        if self.choices:
            func = lambda self, fieldname = name, choicedict = dict(
                self.choices): ",".join(
                    [choicedict.get(value, value) for value in getattr(self, fieldname)])
            setattr(cls, 'get_%s_display' % self.name, func)

    def validate(self, value, model_instance):
        arr_choices = self.get_choices_selected(self.get_choices_default())
        for opt_select in value:
            if (int(opt_select) not in arr_choices):
                raise exceptions.ValidationError(
                    self.error_messages['invalid_choice'] % value)
        return

    def get_choices_selected(self, arr_choices=''):
        if not arr_choices:
            return False
        list = []
        for choice_selected in arr_choices:
            list.append(choice_selected[0])
        return list

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)


class MetaMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class VotingTopic(MetaMixin, models.Model):

    VIEW_PAGE_CHOICES = ((1, "Allow List View"), (2, "Allow Card View"))

    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True)

    list_page_view = MultiSelectField(
        default=[x[0] for x in VIEW_PAGE_CHOICES],
        max_length=250, blank=True, choices=VIEW_PAGE_CHOICES)
    list_page_voting = models.BooleanField(
        "Allow voting on the list page.",
        default=False)

    voting_enabled_date = models.DateTimeField(
        default=datetime.datetime.now, blank=True)
    require_approval = models.BooleanField("Submission Require Approval", default=True)

    def __str__(self):
        return "{title}".format(title=self.title)


class VoteChoice(MetaMixin, models.Model):
    topic = models.ForeignKey(VotingTopic)
    approved = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
