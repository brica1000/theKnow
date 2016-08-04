# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-03 19:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=200)),
                ('order_date', models.DateField(default=django.utils.timezone.now)),
                ('order_details', models.TextField()),
            ],
        ),
    ]