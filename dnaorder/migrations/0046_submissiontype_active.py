# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-15 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnaorder', '0045_auto_20190114_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissiontype',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]