# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-21 21:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dnaorder', '0036_auto_20181221_1335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='name',
            new_name='first_name',
        ),
    ]