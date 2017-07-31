from django.conf.urls import url
# from django.contrib.auth.views import login
from books import views

urlpatterns = [
    url(r'^login-form/$', views.login_form),
    url(r'^login-result/$', views.login_result),
    url(r'^books/$', views.book_list),
    url(r'^login-result/detail/([0-9+])/$', views.book_detail),
    url(r'^books/detail/([0-9+])/$', views.book_detail),
    url(r'^books/logout/$', views.logout_view),
]
