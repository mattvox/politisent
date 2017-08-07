# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20170805_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='id',
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweet_id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
