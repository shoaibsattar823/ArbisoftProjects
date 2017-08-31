# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse

from homeservice.models import Customer, Order
from homeservice.serializers import UserSerializer, CustomerSerializer
from homeservice.serializers import OrderSerializer

from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'customers': reverse('customer-list', request=request, format=format),
        'orders': reverse('order-list', request=request, format=format)
    })


def example_view(request):
    return render(request, 'homeservice/example2.html')


def example_data(request):
    users = []
    for u in User.objects.all():
        users.append(str(u))
    # data = {'data': str(users)}
    return JsonResponse({'data': users})


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    lookup_field = 'username'
    serializer_class = CustomerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class RegisterUser(CreateView):
    success_url = '/'
    template_name = 'homeservice/register.html'
    form_class = UserCreationForm


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

# Issue with order detail because of multiple orders having same pk
'''class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)'''
