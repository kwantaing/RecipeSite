# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-27 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0002_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='readyInMinutes',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
