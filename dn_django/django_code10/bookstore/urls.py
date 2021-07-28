# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/bookstore/all_book/
    url(r'^all_book$', views.all_book_view),
    # 动态 url 的方式
    url(r'^update_book/(?P<book_id>[0-9]+)$', views.update_book_view),
    # 查询参数的方式
    url(r'^delete_book$', views.delete_book_view),
]

if __name__ == '__main__':
    print 1