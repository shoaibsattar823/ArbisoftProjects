from django.conf.urls import url
from blogapp import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^blogs/$', views.BlogsList.as_view(), name='blog-list'),
    url(r'^blogs/(?P<title>[A-Z]*[a-z]*[\w|\W]*[0-9]*)/$',
        views.BlogDetail.as_view(),
        name='blog-detail'),
    url(r'^bloggers/$', views.BloggersList.as_view(), name='blogger-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
