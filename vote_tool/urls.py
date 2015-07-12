from django.conf.urls import url
from .views import VoteTopicListView, VoteTopicCardView, VoteView

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/card/$',
        VoteTopicCardView.as_view(),
        {'view': 'card'},
        name="topic_view_card"),
    url(r'^(?P<slug>[\w-]+)/$',
        VoteTopicListView.as_view(),
        {"view": "list"},
        name="topic_view"),
    url(r'^(?P<slug>[\w-]+)/choice/(?P<choice_id>[\d]+)/$',
        VoteView.as_view(),
        name="topic_view"),
]
