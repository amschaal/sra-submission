# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-06-20 23:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnaorder', '0059_auto_20190611_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='email',
            field=models.EmailField(default='dnatech@ucdavis.edu', max_length=254),
            preserve_default=False,
        ),
    ]
