# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-15 17:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('golfapp', '0033_auto_20170415_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='golfscore',
            name='opponent1',
        ),
        migrations.RemoveField(
            model_name='golfscore',
            name='opponent2',
        ),
        migrations.RemoveField(
            model_name='golfscore',
            name='opponent3',
        ),
    ]
