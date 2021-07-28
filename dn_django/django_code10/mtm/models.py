# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# 多对多关系映射
# Create your models here.
class Author(models.Model):
    name = models.CharField('姓名', max_length=11)


class Book(models.Model):
    title = models.CharField('书名', max_length=11)
    authors = models.ManyToManyField(Author)
