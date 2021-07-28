# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2021-07-16 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_book_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=11, verbose_name='\u59d3\u540d')),
                ('age', models.IntegerField(verbose_name='\u5e74\u9f84')),
                ('email', models.EmailField(max_length=254, verbose_name='\u5e74\u9f84')),
            ],
        ),
    ]
