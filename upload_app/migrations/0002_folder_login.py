# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-09-05 11:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('upload_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='login',
            field=models.CharField(default=datetime.datetime(2017, 9, 5, 11, 39, 0, 59434, tzinfo=utc), max_length=255, verbose_name='Login'),
            preserve_default=False,
        ),
    ]