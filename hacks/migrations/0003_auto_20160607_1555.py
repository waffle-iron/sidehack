# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-07 15:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hacks', '0002_auto_20160606_2234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='githubrepository',
            old_name='repo_creator_id',
            new_name='repo_creator',
        ),
        migrations.RenameField(
            model_name='hack',
            old_name='creator_id',
            new_name='creator',
        ),
        migrations.RenameField(
            model_name='hack',
            old_name='github_repo_id',
            new_name='github_repo',
        ),
    ]
