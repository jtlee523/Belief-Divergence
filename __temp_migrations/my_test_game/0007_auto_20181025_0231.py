# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-10-25 06:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_test_game', '0006_testplayer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testplayer',
            name='group',
        ),
        migrations.RemoveField(
            model_name='testplayer',
            name='participant',
        ),
        migrations.RemoveField(
            model_name='testplayer',
            name='session',
        ),
        migrations.RemoveField(
            model_name='testplayer',
            name='subsession',
        ),
        migrations.DeleteModel(
            name='TestPlayer',
        ),
    ]