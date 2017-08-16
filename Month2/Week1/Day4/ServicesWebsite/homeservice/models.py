# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models


SERVICE_CHOICES = (
                   ('Car Wash', 'Car Wash'),
                   ('Laundry', 'Laundry'),
                   ('Grocery', 'Grocery'),
                   ('Cooking', 'Cook Food')
                   )


class Service(models.Model):
    service_type = models.CharField(max_length=100, unique=True,
                                    choices=SERVICE_CHOICES, default='')

    def __str__(self):
        return self.service_type


class Customer(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length=100, unique=True, default='')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    orders = models.ManyToManyField(Service, through='Order')

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)


@receiver(post_save, sender=User)
def create_customer_profile(sender, **kwargs):
    if kwargs['created']:
        Customer.objects.create(user=kwargs['instance'],
                                username=kwargs['instance'].username,
                                first_name=kwargs['instance'].username)


class Order(models.Model):
    ordered_by = models.ForeignKey(Customer, to_field='username',
                                   db_column='username',
                                   on_delete=models.CASCADE)
    ordered_service = models.ForeignKey(Service, to_field='service_type',
                                        db_column='service_type',
                                        on_delete=models.CASCADE)
    ordered_date = models.DateField()
    status = models.CharField(max_length=50,
                              choices=(
                                       ('Unassigned', 'Unassigned'),
                                       ('Assigned', 'Assigned'),
                                       ('Completed', 'Completed')
                                       ),
                              default='Unassigned')

    def __str__(self):
        return u'%s-%s' % (self.ordered_by, self.ordered_service)
