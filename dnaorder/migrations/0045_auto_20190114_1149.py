# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-14 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnaorder', '0044_submission_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissiontype',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
