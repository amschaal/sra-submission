# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-13 21:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dnaorder', '0003_auto_20180413_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]