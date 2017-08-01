from django.conf.urls import url
from django.contrib.auth import views as auth_views
from books import views

urlpatterns = [
    url(r'^$', views.home_view),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^login-result/$', views.login_result),
    url(r'^books/$', views.book_list),
    # url(r'^login-result/detail/([0-9+])/$', views.book_detail),
    url(r'^detail/([0-9+])/$', views.book_detail),
    url(r'^logout/$', views.logout_view),
    url(r'^book-title/$', views.get_bookTitle),
]
