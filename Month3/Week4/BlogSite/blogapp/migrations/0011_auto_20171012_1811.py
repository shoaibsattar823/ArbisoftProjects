# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0010_auto_20171012_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post',
            field=models.TextField(default=''),
        ),
    ]