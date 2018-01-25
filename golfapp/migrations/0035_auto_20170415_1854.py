# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-15 17:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('golfapp', '0034_auto_20170415_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='golfscore',
            name='opponent1',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opponent1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='opponent2',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opponent2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='opponent3',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opponent3', to=settings.AUTH_USER_MODEL),
        ),
    ]
