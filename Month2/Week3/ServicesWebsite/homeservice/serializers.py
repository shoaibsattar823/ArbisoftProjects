from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Customer, Order


class UserSerializer(serializers.HyperlinkedModelSerializer):
    customer = serializers.HyperlinkedRelatedField(
                   view_name='customer-detail',
                   lookup_field='username',
                   read_only=True,
               )

    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff', 'customer')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
               view_name='user-detail',
               read_only=True
           )
    orders = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ('user', 'first_name', 'last_name', 'orders')

    def get_orders(self, obj):
        ordersset = []
        ordersqueryset = obj.orders.all()
        for order in ordersqueryset:
            ordersset.append(str(order))
        return ordersset


class OrderSerializer(serializers.ModelSerializer):
    ordered_by = serializers.HyperlinkedRelatedField(
                    view_name='customer-detail',
                    lookup_field='username',
                    read_only=True
                 )

    class Meta:
        model = Order
        fields = ('ordered_by', 'ordered_service', 'ordered_date', 'status')
