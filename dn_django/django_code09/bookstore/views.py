# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Book

# Create your views here.


def all_book_view(request):
    all_book = Book.objects.all()
    # 伪删除
    # all_book = Book.objects.filter(is_active=True)
    return render(request, 'bookstore/all_book.html', locals())


# 动态 url 的方式，需要传参
def update_book_view(request, book_id):

    try:
        book = Book.objects.get(id=book_id)
        # 伪删除
        # book = Book.objects.get(id=book_id, is_active=True)
    except Exception as e:
        return HttpResponse('The book is not exist!')

    if request.method == 'GET':
        return render(request, 'bookstore/update_book.html', locals())
    elif request.method == 'POST':
        # 查
        price = request.POST['price']
        market_price = request.POST['market_price']
        # 改
        book.price = price
        book.market_price = market_price
        # 保存
        book.save()

        return HttpResponseRedirect('/bookstore/all_book')


# 查询参数的方式，不需要传参从 get 处获取数据
def delete_book_view(request):
    book_id = request.GET['id']

    if not book_id:
        return HttpResponse('请求异常')
    try:
        book = Book.objects.get(id=book_id)
        # 伪删除
        book = Book.objects.filter(id=book_id, is_active=True)
    except Exception as e:
        return HttpResponse('The book is not exist!')

        # 伪删除
        # # 改
        # book.is_active = False
        # # 保存
        # book.save()

        book.delete()

        return HttpResponseRedirect('/bookstore/all_book')
