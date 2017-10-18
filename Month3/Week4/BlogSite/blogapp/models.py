# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from datetime import datetime


class Blogger(models.Model):
    username = models.OneToOneField(User, default='')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(default='', null=True)

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True, default='')
    post = models.TextField(default='')
    published_date = models.DateField(default=datetime.now)
    blogger = models.ForeignKey(Blogger, default='',
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.title


@receiver(post_save, sender=User)
def create_blogger_profile(sender, **kwargs):
    username = kwargs['instance']
    u1 = sender.objects.get(username=username)
    print('created user: ', u1)
    if kwargs['created']:
        print(kwargs['instance'])
        Blogger.objects.create(username=u1,
                               first_name=kwargs['instance'])


# class BlogPost(models.Model):
#     posted_by = models.ForeignKey(Blogger,
#                                   to_field='username',
#                                   db_column='username',
#                                   on_delete=models.CASCADE)
#     posted_blog = models.ForeignKey(Blog,
#                                     to_field='title',
#                                     db_column='title',
#                                     on_delete=models.CASCADE)
