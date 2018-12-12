# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-06 07:39
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('BeliefDivergence', '0003_player_accuracy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='Green_Probability',
        ),
        migrations.RemoveField(
            model_name='player',
            name='Red_Probability',
        ),
        migrations.RemoveField(
            model_name='player',
            name='Yellow_Probability',
        ),
        migrations.AddField(
            model_name='player',
            name='Green_Probability_guess',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='Green_Urn_Given',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='Red_Probability_guess',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='Red_Urn_Given',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='Yellow_Probability_guess',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='Yellow_Urn_Given',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
