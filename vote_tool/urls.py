from django.conf.urls import url
from .views import (
    VoteTopicListView,
    VoteView, VoteChoiceSubmissionView, VoteChoiceSubmissionSuccessView)

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$',
        VoteTopicListView.as_view(),
        {"view": "list"},
        name="topic_view"),
    url(r'^(?P<slug>[\w-]+)/submit/$',
        VoteChoiceSubmissionView.as_view(),
        name="topic_submit"),
    url(r'^(?P<slug>[\w-]+)/submit/success/$',
        VoteChoiceSubmissionSuccessView.as_view(),
        name="topic_submit_success"),
    url(r'^(?P<slug>[\w-]+)/choice/(?P<choice_id>[\d]+)/$',
        VoteView.as_view(),
        name="topic_vote_view"),
]
