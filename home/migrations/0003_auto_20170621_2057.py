# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 20:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170620_0750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='number',
            name='created',
        ),
        migrations.AddField(
            model_name='number',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='number',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
