from django.contrib import messages
from django.views.generic import DetailView, FormView
from .models import VotingTopic, VoteChoice, Vote
from django.shortcuts import redirect, get_object_or_404


class VoteTopicViewBase(DetailView):
    model = VotingTopic
    template_name = "vote_tool/topic_list.html"
    http_method_names = [u'get']
    context_object_name = 'topic'

    def get_context_data(self, **kwargs):
        context = super(VoteTopicViewBase, self).get_context_data(**kwargs)
        context['view'] = self.view
        return context


class VoteTopicCardView(VoteTopicViewBase):
    view = "card"


class VoteTopicListView(VoteTopicViewBase):
    view = "list"


class VoteView(FormView):
    http_method_names = [u'post']
    context_object_name = 'topic'

    def dispatch(self, request, *args, **kwargs):
        self.topic_slug = kwargs.get('slug')
        self.choice_id = kwargs.get('choice_id')
        self.choice = get_object_or_404(
            VoteChoice,
            id=self.choice_id,
            topic__slug=self.topic_slug)
        return super(VoteView, self).dispatch(request, *args, **kwargs)

    def form_invalid(self, form):
        messages.error(self.request, 'Unable to save vote.')
        return redirect(self.get_success_url())

    def form_valid(self, form):
        messages.info(self.request, 'Vote submitted.')
        return redirect(self.get_success_url())
