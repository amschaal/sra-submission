# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-08-07 20:33
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dnaorder', '0061_submission_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='variables',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]
