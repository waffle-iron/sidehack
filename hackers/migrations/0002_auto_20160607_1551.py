# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-07 15:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hacker',
            old_name='org_id',
            new_name='org',
        ),
    ]
