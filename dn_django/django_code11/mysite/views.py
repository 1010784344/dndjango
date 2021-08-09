# -*- coding: utf-8 -*-
from django.http import HttpResponse
import time
from django.views.decorators.cache import cache_page
from django.shortcuts import render


@cache_page(5)
def test_cache(request):

    t = time.time()

    return HttpResponse('t is %s' % t)


def test_mw(request):
    print '---test_mw view---'

    return HttpResponse('---test_mw---')


def test_csrf(request):
    if request.method == 'GET':
        return render(request, 'test_csrf.html')
    elif request.method == 'POST':
        return HttpResponse('---test_csrf is ok---')
