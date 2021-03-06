# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-10 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documenttypeassimilation',
            name='assimilation_criteria',
        ),
        migrations.AlterField(
            model_name='applicantassimilationcriteria',
            name='additional_criteria',
            field=models.CharField(blank=True, choices=[('CRITERIA_1', 'CRITERIA_1'), ('CRITERIA_2', 'CRITERIA_2'), ('CRITERIA_3', 'CRITERIA_3'), ('CRITERIA_4', 'CRITERIA_4'), ('CRITERIA_5', 'CRITERIA_5'), ('CRITERIA_6', 'CRITERIA_6'), ('CRITERIA_7', 'CRITERIA_7')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='applicantassimilationcriteria',
            name='criteria',
            field=models.CharField(choices=[('CRITERIA_1', 'CRITERIA_1'), ('CRITERIA_2', 'CRITERIA_2'), ('CRITERIA_3', 'CRITERIA_3'), ('CRITERIA_4', 'CRITERIA_4'), ('CRITERIA_5', 'CRITERIA_5'), ('CRITERIA_6', 'CRITERIA_6'), ('CRITERIA_7', 'CRITERIA_7')], max_length=50),
        ),
        migrations.AlterField(
            model_name='applicationassimilationcriteria',
            name='additional_criteria',
            field=models.CharField(blank=True, choices=[('CRITERIA_1', 'CRITERIA_1'), ('CRITERIA_2', 'CRITERIA_2'), ('CRITERIA_3', 'CRITERIA_3'), ('CRITERIA_4', 'CRITERIA_4'), ('CRITERIA_5', 'CRITERIA_5'), ('CRITERIA_6', 'CRITERIA_6'), ('CRITERIA_7', 'CRITERIA_7')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='applicationassimilationcriteria',
            name='criteria',
            field=models.CharField(choices=[('CRITERIA_1', 'CRITERIA_1'), ('CRITERIA_2', 'CRITERIA_2'), ('CRITERIA_3', 'CRITERIA_3'), ('CRITERIA_4', 'CRITERIA_4'), ('CRITERIA_5', 'CRITERIA_5'), ('CRITERIA_6', 'CRITERIA_6'), ('CRITERIA_7', 'CRITERIA_7')], max_length=50),
        ),
        migrations.DeleteModel(
            name='DocumentTypeAssimilation',
        ),
    ]
