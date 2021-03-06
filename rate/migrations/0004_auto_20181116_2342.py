# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-16 20:42
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0003_auto_20181116_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='content',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='project',
            name='design',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='project',
            name='usability',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
