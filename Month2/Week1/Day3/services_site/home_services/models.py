# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import datetime


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    email = models.EmailField(blank=True)

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)


@receiver(post_save, sender=User)
def create_customer_profile(sender, **kwargs):
    print sender.objects.all()
    print kwargs['instance']
    if kwargs['created']:
        Customer.objects.create(user=kwargs['instance'])


class Service(models.Model):
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='Unassigned')
    ordered_by = models.ManyToManyField(Customer, blank=True)
    ordered_date = models.DateField(default=datetime.date.today)
    completed_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.category
