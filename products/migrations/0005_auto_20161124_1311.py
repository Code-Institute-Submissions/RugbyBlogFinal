# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20161124_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Image',
            field=models.ImageField(default='media/images/cap.jpg', upload_to='media/images'),
        ),
    ]
