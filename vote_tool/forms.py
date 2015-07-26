from django import forms
from .models import Vote, VoteChoice


class VoteForm(forms.ModelForm):

    class Meta:
        model = Vote
        fields = []

    def __init__(self, user, topic_slug, choice, *args, **kwargs):
        self.user = user
        self.topic_slug = topic_slug
        self.choice = choice
        super(VoteForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(VoteForm, self).clean()
        if Vote.objects.filter(choice__topic__slug=self.topic_slug, user=self.user):
            raise forms.ValidationError(
                "You may only vote once.")
        return cleaned_data


class VoteChoiceForm(forms.ModelForm):

    class Meta:
        model = VoteChoice
        fields = ['text', 'description', 'picture', 'link', 'link_text']
