# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 10:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(db_index=True, max_length=100)),
                ('Age', models.IntegerField(blank=True)),
                ('BookingD', models.DateField(blank=True, default='2017-01-01')),
                ('BookingT', models.TimeField(blank=True, default='00:00:00')),
                ('Description', models.TextField(blank=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductTitle', models.CharField(db_index=True, max_length=200)),
                ('ProductDescription', models.TextField(db_index=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServiceTitle', models.CharField(db_index=True, max_length=200)),
                ('ServiceDescription', models.TextField(db_index=True, max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='appointments',
            name='ServiceName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pservices.Service'),
        ),
    ]
