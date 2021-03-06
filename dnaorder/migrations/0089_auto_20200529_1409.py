# Generated by Django 2.2.6 on 2020-05-29 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('dnaorder', '0088_remove_submission_sra_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='sites.Site')),
            ],
        ),
        migrations.DeleteModel(
            name='SubmissionStatus',
        ),
    ]
