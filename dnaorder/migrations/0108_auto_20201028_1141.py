# Generated by Django 2.2.6 on 2020-10-28 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnaorder', '0107_auto_20201028_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='status',
            field=models.CharField(default='Submitted', max_length=50),
        ),
    ]