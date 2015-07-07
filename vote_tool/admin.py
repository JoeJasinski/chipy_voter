from django.contrib import admin
from django import forms
from .models import VotingTopic, VoteChoice


class VotingTopicAdminForm(forms.ModelForm):

    class Meta:
        exclude = ['created_at', 'modified_at']
        model = VotingTopic


class VotingTopicInline(admin.TabularInline):
    model = VoteChoice


class VotingTopicAdmin(admin.ModelAdmin):
    form = VotingTopicAdminForm
    prepopulated_fields = {"slug": ("title",)}
    inlines = [VotingTopicInline, ]


admin.site.register(VotingTopic, VotingTopicAdmin)
