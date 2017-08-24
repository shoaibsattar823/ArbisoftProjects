from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Customer, Order


class UserSerializer(serializers.HyperlinkedModelSerializer):
    customer = serializers.HyperlinkedRelatedField(
                   view_name='customer-detail',
                   read_only=True
               )

    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff', 'customer')


class CustomerSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(
               view_name='user-detail',
               read_only=True
           )

    class Meta:
        model = Customer
        fields = ('user', 'first_name', 'last_name', 'orders')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('ordered_by', 'ordered_service', 'ordered_date', 'status')
