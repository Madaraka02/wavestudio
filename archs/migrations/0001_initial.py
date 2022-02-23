# Generated by Django 4.0.2 on 2022-02-23 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('email', models.CharField(max_length=300)),
                ('message', models.TextField()),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('testimony', models.TextField()),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='images')),
            ],
            options={
                'verbose_name_plural': 'Feedbacks',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.FileField(upload_to='logos')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.FileField(null=True, upload_to='projimages')),
                ('video', models.FileField(blank=True, null=True, upload_to='projvideos')),
                ('description', models.TextField(blank=True, null=True)),
                ('completed', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Projects',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='ProjectImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='projimages')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archs.project')),
            ],
            options={
                'verbose_name_plural': 'ProjectImages',
                'ordering': ('-id',),
            },
        ),
    ]