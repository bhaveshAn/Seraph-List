# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-09-17 07:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='lastname',
        ),
    ]
