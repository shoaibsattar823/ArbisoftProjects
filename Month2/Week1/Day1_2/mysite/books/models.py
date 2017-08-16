# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=30, default='')
    website = models.URLField(default='')


def create_profile(sender, **kwargs):
    if kwargs['created']:
        UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, User)


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class UserManager(models.Manager):
    def get_queryset(self):
        return super(UserManager,
                     self).get_queryset().filter(last_name='Barry')


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True)

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    objects = models.Manager()
    barry = UserManager()


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return '/'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.publication_date:
            self.publication_date = datetime.date.today()
            super(Book, self).save(*args, **kwargs)
            print('Book saved now!')
        else:
            super(Book, self).save(*args, **kwargs)


@receiver(pre_save, sender=Book)
def checkDate(instance, **kwargs):
    if instance.publication_date is not None:
        print('Date Field OK!\n which is: ', instance.publication_date)
# pre_save.connect(checkDate, Book)
