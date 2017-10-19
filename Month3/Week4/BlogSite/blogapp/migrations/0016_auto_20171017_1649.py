# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0015_auto_20171017_1644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blogger',
            new_name='author',
        ),
        migrations.AddField(
            model_name='blogger',
            name='blogs',
            field=models.ManyToManyField(to='blogapp.Blog'),
        ),
    ]