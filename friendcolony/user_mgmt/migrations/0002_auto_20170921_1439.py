# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-21 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_mgmt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crickethangoutplace',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='hangoutplaces',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]