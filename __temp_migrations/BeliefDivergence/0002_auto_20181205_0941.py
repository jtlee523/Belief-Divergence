# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-05 14:41
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('BeliefDivergence', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='Assigned_Green',
            field=otree.db.models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='Assigned_Red',
            field=otree.db.models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='Assigned_Yellow',
            field=otree.db.models.FloatField(null=True),
        ),
    ]
