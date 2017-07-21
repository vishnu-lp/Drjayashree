# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-17 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pservices', '0002_auto_20170609_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ProductImage',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='service',
            name='ServiceImage',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProductDescription',
            field=models.TextField(db_index=True, max_length=1500),
        ),
        migrations.AlterField(
            model_name='service',
            name='ServiceDescription',
            field=models.TextField(db_index=True, max_length=1500),
        ),
    ]