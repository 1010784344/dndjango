# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# 一对一关系映射
# Create your models here.
class Author(models.Model):
    name = models.CharField('姓名', max_length=11)


class Wife(models.Model):
    name = models.CharField('姓名', max_length=11)
    # 通常外键属性叫对应模型类的类名的小写
    author = models.OneToOneField(Author)






