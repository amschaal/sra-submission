# Generated by Django 2.2.6 on 2020-03-13 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dnaorder', '0085_sample'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='sample',
            unique_together={('name', 'submission'), ('id_suffix', 'submission')},
        ),
    ]