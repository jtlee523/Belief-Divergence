# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-05 18:11
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('BeliefDivergence', '0002_auto_20181205_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='Accuracy',
            field=otree.db.models.FloatField(null=True),
        ),
    ]