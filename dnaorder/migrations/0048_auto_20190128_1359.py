# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-28 21:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dnaorder', '0047_auto_20190122_1028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='payment_info',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='payment_type',
        ),
    ]
