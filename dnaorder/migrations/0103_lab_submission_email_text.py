# Generated by Django 2.2.6 on 2020-09-17 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnaorder', '0102_auto_20200818_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='submission_email_text',
            field=models.TextField(blank=True, default=''),
        ),
    ]
