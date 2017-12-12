# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.http import HttpResponseRedirect
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import Blog, Blogger
from .serializers import BlogSerializer, BloggerSerializer, UserSerializer
from django.contrib.auth.models import User


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'blogs': reverse('blog-list', request=request, format=format),
        'bloggers': reverse('blogger-list', request=request, format=format)
    })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retreive(self, request, pk=None):
        if pk == 'i':
            return Response(UserSerializer(request.user,
                            context={'request': request}).data)
        return super(UserViewSet, self).retreive(request, pk)


class BlogsList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, format=None):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddBlog(generics.CreateAPIView):
    serializer_class = BlogSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, *args, **kwargs):
        blogs = Blog.objects.all()

        for i in range(0, len(blogs)):
            print(blogs[i].title, ' ', blogs[i].blogger)
            # blogs[i].blogger = [b[0] for b in blogs[i].blogger]
        print(list(blogs))
        myBlogs = []
        for b in blogs:
            myBlogs.append({'title': b.title, 'post': b.post,
                           'pub_date': b.pub_date, 'blogger': b.blogger})
        return Response({'serializer': myBlogs},)


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    lookup_field = 'title'
    serializer_class = BlogSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BloggersList(generics.ListCreateAPIView):
    queryset = Blogger.objects.all()
    serializer_class = BloggerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
