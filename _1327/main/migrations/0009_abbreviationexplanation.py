# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-15 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20160806_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbbreviationExplanation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbreviation', models.CharField(max_length=255, unique=True, verbose_name='Abbreviation')),
                ('explanation', models.CharField(max_length=255, verbose_name='Explanation')),
            ],
        ),
    ]
