# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-01 22:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minutes', '0008_add_on_delete'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='minutesdocument',
            options={'base_manager_name': 'objects', 'permissions': (('view_minutesdocument', 'User/Group is allowed to view those minutes'),), 'verbose_name': 'Minutes', 'verbose_name_plural': 'Minutes'},
        ),
    ]
