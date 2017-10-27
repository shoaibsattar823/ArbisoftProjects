from django.conf.urls import url
from blogapp import views

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^blogs/$', views.BlogsList.as_view(), name='blog-list'),
    url(r'^blogs/(?P<title>[A-Z]*[a-z]*[\w|\W]*[0-9]*)/$',
        views.BlogDetail.as_view(),
        name='blog-detail'),
    url(r'^bloggers/$', views.BloggersList.as_view(), name='blogger-list'),
    url(r'^add-blog/$', views.AddBlog.as_view(), name='add-blog'),
    url(r'^obtain_auth_token/$', obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
