# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeservice', '0007_auto_20170815_1804'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ServiceStatus',
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
    ]
