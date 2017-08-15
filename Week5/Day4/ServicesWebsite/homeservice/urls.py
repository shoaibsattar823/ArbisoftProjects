from django.conf.urls import url
from django.contrib.auth import views as auth_views
from homeservice import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(template_name='homeservice/index.html')),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^register/$', views.RegisterUser.as_view()),
    url(r'^logout/$', views.logout_view),
    url(r'^request/$', views.NewRequest.as_view()),
    url(r'^requests-detail/$', views.RequestDetail.as_view()),
]
