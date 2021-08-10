# -*- coding: utf-8 -*-
from django.http import HttpResponse
import time
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from django.core.paginator import Paginator
import csv

# 缓存
@cache_page(5)
def test_cache(request):

    t = time.time()

    return HttpResponse('t is %s' % t)


# 中间件
def test_mw(request):
    print '---test_mw view---'

    return HttpResponse('---test_mw---')


# csrf 验证
def test_csrf(request):
    if request.method == 'GET':
        return render(request, 'test_csrf.html')
    elif request.method == 'POST':
        return HttpResponse('---test_csrf is ok---')


# 分页
def test_page(request):

    # /test_page?page=1
    page_num = request.GET.get('page', 1)
    all_data = ['a', 'b', 'c', 'd', 'e']
    paginator = Paginator(all_data, 2)
    c_page = paginator.page(int(page_num))

    return render(request, 'test_page.html', locals())


# 下载csv 文件
def test_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="mybook.csv"'

    all_data = ['a', 'b', 'c', 'd']

    my_writer = csv.writer(response)
    my_writer.writerow(all_data)

    return response


# 下载分页的 csv 文件
def make_page_csv(request):

    # /make_page_csv?page=1
    page_num = request.GET.get('page', 1)
    all_data = ['a', 'b', 'c', 'd', 'e']
    paginator = Paginator(all_data, 2)
    c_page = paginator.page(int(page_num))

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="page_%s.csv"' % page_num

    my_writer = csv.writer(response)

    for data in c_page:

        my_writer.writerow([data])

    return response













