# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-14 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0009_auto_20161109_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='state',
            field=models.CharField(blank=True, choices=[('NEW', 'NEW'), ('SUBMITTED', 'SUBMITTED')], max_length=35, null=True),
        ),
    ]