# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 19:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170606_1939'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='btleevent',
            options={'ordering': ('arrival_time',), 'verbose_name_plural': 'btleevents'},
        ),
    ]
