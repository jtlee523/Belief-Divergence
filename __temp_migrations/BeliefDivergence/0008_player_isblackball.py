# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-06 19:51
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('BeliefDivergence', '0007_auto_20181206_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='isBlackBall',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
