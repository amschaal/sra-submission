# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-11 22:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dnaorder', '0020_auto_20180911_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='sample_form',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='sra_form',
        ),
        migrations.RemoveField(
            model_name='submissiontype',
            name='end_column',
        ),
        migrations.RemoveField(
            model_name='submissiontype',
            name='form',
        ),
        migrations.RemoveField(
            model_name='submissiontype',
            name='has_submission_fields',
        ),
        migrations.RemoveField(
            model_name='submissiontype',
            name='header_index',
        ),
        migrations.RemoveField(
            model_name='submissiontype',
            name='original',
        ),
        migrations.RemoveField(
            model_name='submissiontype',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='submissiontype',
            name='show',
        ),
        migrations.RemoveField(
            model_name='submissiontype',
            name='skip_rows',
        ),
        migrations.RemoveField(
            model_name='submissiontype',
            name='start_column',
        ),
        migrations.RemoveField(
            model_name='submissiontype',
            name='submission_end_column',
        ),
        migrations.RemoveField(
            model_name='submissiontype',
            name='submission_header_row',
        ),
        migrations.RemoveField(
            model_name='submissiontype',
            name='submission_skip_rows',
        ),
        migrations.RemoveField(
            model_name='submissiontype',
            name='submission_start_column',
        ),
        migrations.RemoveField(
            model_name='submissiontype',
            name='version',
        ),
    ]
