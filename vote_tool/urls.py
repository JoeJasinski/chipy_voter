from django.conf.urls import include, url
from .views import VoteTopicView

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', VoteTopicView.as_view()),
]
