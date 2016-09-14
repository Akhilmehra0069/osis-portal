# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-14 07:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0002_domain'),
        ('admission', '0008_auto_20160909_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationAssimilationCriteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_criteria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='application_additional_criteria', to='reference.AssimilationCriteria')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admission.Application')),
                ('criteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reference.AssimilationCriteria')),
            ],
        ),
        migrations.AddField(
            model_name='applicantassimilationcriteria',
            name='additional_criteria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicant_additional_criteria', to='reference.AssimilationCriteria'),
        ),
    ]