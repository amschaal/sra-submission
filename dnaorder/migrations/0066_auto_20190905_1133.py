# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-09-05 18:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dnaorder', '0065_auto_20190830_1111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vocabulary',
            old_name='name',
            new_name='id',
        ),
    ]
