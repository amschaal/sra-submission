# Generated by Django 2.2.6 on 2020-08-13 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dnaorder', '0099_prefixid_num_digits'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissiontype',
            name='default_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dnaorder.PrefixID'),
        ),
    ]
