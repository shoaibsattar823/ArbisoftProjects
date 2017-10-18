# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

from .models import Blog, Blogger
from .serializers import BlogSerializer, BloggerSerializer
# from .forms import BlogForm


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'blogs': reverse('blog-list', request=request, format=format),
        'bloggers': reverse('blogger-list', request=request, format=format)
    })


class BlogsList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    lookup_field = 'title'
    serializer_class = BlogSerializer


class BloggersList(generics.ListCreateAPIView):
    queryset = Blogger.objects.all()
    serializer_class = BloggerSerializer


# def new_blog(request):
#     if request.method == 'POST':
#         form = BlogForm(request.POST)
#
#         if form.is_valid():
#             myform = form.save(commit=False)
#             b = Blog(title=myform.title,
#                      post=myform.post,
#                      blogger=myform.blogger)
#             b.save()
#             HttpResponseRedirect('/')
#     else:
#         form = BlogForm()
#     return render(request, 'blogapp/blog-form.html', {'form': form})
