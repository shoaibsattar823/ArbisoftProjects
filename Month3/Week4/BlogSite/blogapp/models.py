# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from datetime import datetime

from rest_framework.authtoken.models import Token


class Blogger(models.Model):
    username = models.OneToOneField(User, default='')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(default='', null=True)

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Blog(models.Model):
    bloggerObjs = Blogger.objects.all()
    bloggerNames = ()
    for b in bloggerObjs:
        bloggerNames += ((b.first_name, b.first_name+' '+b.last_name), )

    title = models.CharField(max_length=100, unique=True, default='')
    post = models.TextField(default='')
    published_date = models.DateField(default=datetime.now)
    # blogger = models.ForeignKey(Blogger, default='',
    #                             on_delete=models.CASCADE)
    blogger = models.CharField(max_length=100, choices=bloggerNames)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if(self.blogger not in [str(n[1]).strip() for n in self.bloggerNames]):
            raise Exception('Name not in the list of Bloggers')
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


@receiver(post_save, sender=User)
def init_new_user(sender, instance, signal, created, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_blogger_profile(sender, **kwargs):
    username = kwargs['instance']
    u1 = sender.objects.get(username=username)
    print('created user: ', u1)
    if kwargs['created']:
        print(kwargs['instance'])
        Blogger.objects.create(username=u1,
                               first_name=kwargs['instance'])
