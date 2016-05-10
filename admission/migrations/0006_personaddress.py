# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-04 10:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0001_initial'),
        ('admission', '0005_auto_20160404_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('LEGAL', 'Legal'), ('CONTACT', 'Contact')], max_length=20)),
                ('street', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=6)),
                ('complement', models.CharField(blank=True, max_length=255, null=True)),
                ('postal_code', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reference.Country')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admission.Person')),
            ],
        ),
    ]