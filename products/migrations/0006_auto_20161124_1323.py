# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 13:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20161124_1311'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='products',
            new_name='Product',
        ),
    ]
