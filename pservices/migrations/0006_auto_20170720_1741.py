# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-20 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pservices', '0005_auto_20170717_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ProductImage',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='ServiceImage',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
