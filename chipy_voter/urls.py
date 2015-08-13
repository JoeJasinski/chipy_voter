from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib.flatpages import views
from django.contrib import admin

urlpatterns = [
    url(r'^login/$', 'chipy_voter.apps.users.views.login',),
    url(r'^logout/$', 'chipy_voter.apps.users.views.logout',),
    url(r'^admin/', include(admin.site.urls)),
    url('topics/', include('vote_tool.urls', namespace='topics')),
    #url('^', include('chipy_voter.apps.users.urls', namespace='social')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^(?P<url>.*/)$', views.flatpage),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
