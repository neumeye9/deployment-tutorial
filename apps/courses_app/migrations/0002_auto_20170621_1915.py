# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-21 19:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='descriptoion',
            new_name='description',
        ),
    ]