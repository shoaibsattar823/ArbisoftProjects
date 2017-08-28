# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeservice', '0005_auto_20170815_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='service_status',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Unassigned', 'Unassigned'), ('Assigned', 'Assigned'), ('Completed', 'Completed')], default='Unassigned', max_length=50),
        ),
    ]
