from django.conf.urls import url, include
from django.contrib import admin

# from rest_framework import routers

# from blogapp import views

# router = routers.DefaultRouter()
# router.register('blogs', views.BlogViewSet)
# router.register('bloggers', views.BloggerViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^create-blog', views.new_blog),
    url(r'^', include('blogapp.urls')),
    url(r'api-auth/', include('rest_framework.urls',
        namespace='rest_framework'))
    # url(r'^', include(router.urls)),
    # url(r'^api_auth/', include('rest_framework.urls'),
    #    namespace='rest_framework')
]
