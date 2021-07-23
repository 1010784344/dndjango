# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField("书名", max_length=50, default='', unique=True)
    pub = models.CharField("出版社", max_length=100, default='')
    price = models.DecimalField("价格", max_digits=7, decimal_places=2, default=0.0)
    market_price = models.DecimalField("零售价", max_digits=7, decimal_places=2, default=0.0)
    is_active = models.BooleanField('是否活跃', default=True)
    # 改变模型类对应的表名
    class Meta:
        db_table = 'book'

    # 定义查询结果的输出样式
    def __str__(self):
        return '%s_%s_%s_%s' % (self.title, self.pub, self.price, self.market_price)


class Author(models.Model):
    name = models.CharField('姓名', max_length=11)
    age = models.IntegerField('年龄', default=1)
    email = models.EmailField('年龄', null=True)

    class Meta:
        db_table = 'author'
