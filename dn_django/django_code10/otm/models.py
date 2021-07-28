# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
# 一对一关系映射
class Publisher(models.Model):
    name = models.CharField('出版社', max_length=50)


class Book(models.Model):
    title = models.CharField('书名', max_length=11)
    publisher = models.ForeignKey(Publisher)

