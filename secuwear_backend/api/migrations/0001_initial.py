# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 20:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BtleEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cap_length', models.IntegerField()),
                ('layers', models.TextField()),
                ('highest_layer', models.CharField(max_length=100)),
                ('epoch_time', models.FloatField()),
                ('arrival_time', models.DateTimeField(auto_now_add=True)),
                ('access_address', models.CharField(max_length=200)),
                ('advertising_address', models.CharField(max_length=300)),
                ('advertising_header', models.CharField(max_length=200)),
                ('crc', models.CharField(max_length=200)),
                ('data', models.CharField(max_length=300, null=True)),
                ('ppi_flags', models.CharField(max_length=100)),
                ('ppi_version', models.CharField(max_length=200)),
                ('ppi_dlt', models.CharField(max_length=100)),
                ('ppi_header_length', models.CharField(max_length=100)),
                ('ppi_reserved', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('arrival_time',),
                'verbose_name_plural': 'btles',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('clocktimedifference', models.DurationField(blank=True, null=True)),
                ('eventtype', models.CharField(blank=True, max_length=1024)),
                ('event', models.TextField(blank=True)),
                ('codereference', models.TextField(blank=True)),
                ('domain', models.CharField(blank=True, max_length=1024)),
            ],
            options={
                'verbose_name_plural': 'events',
            },
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=1024)),
                ('description', models.TextField(blank=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'experiments',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roles', models.CharField(default='{"admin": false, "researcher": false, "subject": true}', max_length=200)),
                ('gender', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('educationlevel', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('ip', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=1024)),
                ('description', models.TextField(blank=True)),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='runs', to='api.Experiment')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='runs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'runs',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='api.Run'),
        ),
        migrations.AddField(
            model_name='btleevent',
            name='run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='btleEvents', to='api.Run'),
        ),
    ]
