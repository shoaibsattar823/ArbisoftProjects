# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeservice', '0008_auto_20170815_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='urgency',
            field=models.CharField(choices=[('Urgent', 'Urgent'), ('Normal', 'Normal')], default='', max_length=30),
        ),
    ]
