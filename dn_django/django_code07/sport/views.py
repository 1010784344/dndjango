# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index_view(request):
    return HttpResponse('这是体育频道首页！')
