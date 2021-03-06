# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 21:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20171102_2344'),
    ]

    operations = [
        migrations.CreateModel(
            name='AndroidEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrivaltime', models.DateTimeField(auto_now_add=True)),
                ('fragment', models.CharField(max_length=500)),
                ('setup', models.TextField(blank=True)),
                ('boardReady', models.CharField(max_length=500)),
                ('request', models.TextField(blank=True)),
                ('response', models.TextField(blank=True)),
            ],
        ),
    ]
