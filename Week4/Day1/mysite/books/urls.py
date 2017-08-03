from django.conf.urls import url
from django.contrib.auth import views as auth_views
from books import views
from books.views import Home_view, Book_list, Book_detail

urlpatterns = [
    url(r'^$', Home_view.as_view()),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^login-result/$', views.login_result),
    url(r'^books/$', Book_list.as_view()),
    # url(r'^login-result/detail/([0-9+])/$', views.book_detail),
    # url(r'^detail/[0-9]+', Book_detail.as_view()),
    url(r'^detail/(?P<pk>\d+)/$', Book_detail.as_view(template_name='books/detail.html'), name='detail'),
    url(r'^logout/$', views.logout_view),
    url(r'^book-form/$', views.get_BookForm),
]
