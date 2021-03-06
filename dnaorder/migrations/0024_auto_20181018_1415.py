# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-18 21:15
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnaorder', '0023_submissiontype_examples'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='cancelled',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='submissiontype',
            name='examples',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=list),
        ),
    ]
