from django.conf.urls import url
from django.contrib.auth import views as auth_views
from home_services import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(
                              template_name='home_services/index.html')),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^register/$', views.RegisterCustomer.as_view()),
    url(r'^logout/$', views.logout_view),
    url(r'^new-request/$', views.RequestService.as_view())
]
