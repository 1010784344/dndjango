# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2021-07-17 04:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_author'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='book',
            table='book',
        ),
    ]
