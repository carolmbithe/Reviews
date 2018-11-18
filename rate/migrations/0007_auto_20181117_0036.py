# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-16 21:36
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0006_auto_20181117_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='content',
            field=models.PositiveIntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='project',
            name='design',
            field=models.PositiveIntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='project',
            name='usability',
            field=models.PositiveIntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]
