# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20161124_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
