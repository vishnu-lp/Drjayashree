# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pservices', '0004_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='Description',
            field=models.TextField(blank=True),
        ),
    ]
