# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-04 20:33
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('my_test_game', '0016_auto_20181204_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='isGray',
        ),
        migrations.AddField(
            model_name='player',
            name='isGray1',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')]),
        ),
    ]