from django.shortcuts import render
from django.views.generic import DetailView
from .models import VotingTopic

class VoteTopicView(DetailView):
    model = VotingTopic
    template_name = "vote_tool/topic_list.html"
    http_method_names = [u'get']
    context_object_name = 'topic'

    def get_context_data(self, **kwargs):
        return_value = super(VoteTopicView, self).get_context_data(**kwargs)
        return return_value
