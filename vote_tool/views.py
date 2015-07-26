from django.contrib import messages
from django.views.generic import DetailView, FormView, CreateView, TemplateView
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import VotingTopic, VoteChoice
from .forms import VoteForm, VoteChoiceForm
from django.shortcuts import redirect, get_object_or_404


class VoteTopicListView(DetailView):
    model = VotingTopic
    template_name = "vote_tool/topic_list.html"
    http_method_names = [u'get']
    context_object_name = 'topic'

    def get_context_data(self, **kwargs):
        if self.request.GET.get('view') == "list":
            self.view = "list"
        else:
            self.view = "card"
        context = super(VoteTopicListView, self).get_context_data(**kwargs)
        context['view'] = self.view
        return context


class VoteChoiceSubmissionView(CreateView):
    http_method_names = [u'post', u'get']
    template_name = "vote_tool/vote_choice_submit.html"
    model = VoteChoice
    form_class = VoteChoiceForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.topic_slug = kwargs.get('slug')
        self.topic = get_object_or_404(
            VotingTopic,
            slug=self.topic_slug)
        return super(VoteChoiceSubmissionView, self).dispatch(
            request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.topic = self.topic
        self.object.save()
        return super(VoteChoiceSubmissionView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(VoteChoiceSubmissionView, self).get_context_data(
            **kwargs)
        context['topic'] = self.topic
        return context

    def get_success_url(self):
        url = reverse('topics:topic_submit_success', args=[self.topic_slug])
        return url


class VoteChoiceSubmissionSuccessView(TemplateView):
    template_name = "vote_tool/vote_choice_submit_success.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.topic_slug = kwargs.get('slug')
        self.topic = get_object_or_404(
            VotingTopic,
            slug=self.topic_slug)
        return super(VoteChoiceSubmissionSuccessView, self).dispatch(
            request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(VoteChoiceSubmissionSuccessView, self).get_context_data(
            **kwargs)
        context['topic'] = self.topic
        return context


class VoteView(FormView):
    http_method_names = [u'post']
    context_object_name = 'topic'
    form_class = VoteForm

    def get_success_url(self):
        url = reverse('topics:topic_view', args=[self.topic_slug])
        return url

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.topic_slug = kwargs.get('slug')
        self.choice_id = kwargs.get('choice_id')
        self.user = request.user
        self.choice = get_object_or_404(
            VoteChoice,
            id=self.choice_id,
            topic__slug=self.topic_slug)
        return super(VoteView, self).dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(
            user=self.user, topic_slug=self.topic_slug,
            choice=self.choice, **self.get_form_kwargs())

    def form_invalid(self, form):
        messages.error(self.request, 'Unable to save vote. %s' % form.errors)
        return redirect(self.get_success_url())

    def form_valid(self, form):
        messages.info(self.request, 'Vote submitted.')
        vote = form.save(commit=False)
        vote.user = self.request.user
        vote.choice = self.choice
        vote.value = 1
        vote.save()
        return redirect(self.get_success_url())
