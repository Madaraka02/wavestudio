# Generated by Django 4.0.2 on 2022-02-24 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archs', '0002_project_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
    ]
