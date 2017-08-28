from django.conf.urls import url, include
from homeservice import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url('^$', views.api_root),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(),
        name='user-detail'),
    url(r'^customers/$', views.CustomerList.as_view(), name='customer-list'),
    url(r'^customers/(?P<username>[a-z]+[0-9]*)/$',
        views.CustomerDetail.as_view(),
        name='customer-detail'),
    url(r'^orders/$', views.OrderList.as_view(), name='order-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
