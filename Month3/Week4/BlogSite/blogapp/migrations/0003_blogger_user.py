# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 09:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0002_auto_20171011_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogger',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]