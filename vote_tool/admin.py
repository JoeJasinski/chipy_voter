from django.contrib import admin
from django.conf.urls import url
from django import forms
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from .models import VotingTopic, VoteChoice, Vote


class VotingTopicAdminForm(forms.ModelForm):

    class Meta:
        exclude = ['created_at', 'modified_at']
        model = VotingTopic


class VotingTopicInline(admin.StackedInline):
    model = VoteChoice
    raw_id_fields = ['user']
    readonly_fields = ['created_at', 'updated_at']
    extra = 0


class VotingTopicAdmin(admin.ModelAdmin):
    form = VotingTopicAdminForm
    prepopulated_fields = {"slug": ("title",)}
    inlines = [VotingTopicInline, ]

    def get_urls(self):
        urls = super(VotingTopicAdmin, self).get_urls()
        info = self.model._meta.app_label, self.model._meta.model_name
        vote_urls = [
            url(r'^(\d+)/votes/$', self.vote_list, name='%s_%s_votes' % info),
        ]
        return vote_urls + urls

    def vote_list(self, request, object_id, *args, **kwargs):
        opts = self.model._meta
        topic = get_object_or_404(self.model, id=object_id)
        context = dict(
           # Include common variables for rendering the admin template.
           self.admin_site.each_context(request),
           # Anything else you want in the context...
           opts=opts,
           topic=topic,
           title="Votes",
        )
        return TemplateResponse(request, "admin/vote_list.html", context)


class VoteAdmin(admin.ModelAdmin):
    raw_id_fields = ['user']
    list_display = ['get_topic']
    readonly_fields = ['get_topic', 'created_at', 'updated_at']

    def get_topic(self, obj):
        return obj.choice.topic
    get_topic.short_description = "Topic"

    fieldsets = (
        (None, {
                'fields': (('get_topic', 'choice', 'user',),)
            }),
            ('Meta', {
                'classes': ('collapse',),
                'fields': (('created_at', 'updated_at'),),
            }),
        )

admin.site.register(VotingTopic, VotingTopicAdmin)
admin.site.register(Vote, VoteAdmin)
