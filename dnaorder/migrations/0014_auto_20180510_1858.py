# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-10 18:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dnaorder', '0013_submission_submission_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submissiontype',
            old_name='submission_value_row',
            new_name='submission_skip_rows',
        ),
    ]
