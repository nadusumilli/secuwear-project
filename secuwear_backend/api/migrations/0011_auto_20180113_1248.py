# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-13 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20180112_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='run',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
