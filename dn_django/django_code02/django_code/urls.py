# -*- coding: utf-8 -*-
"""django_code URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django_code import views

urlpatterns = [

    # django 管理后台的路由
    url(r'^admin/$', admin.site.urls),

    # http://127.0.0.1:8000/    (匹配根目录)
    url(r'^$', views.index_view),

    # http://127.0.0.1:8000/page/2-100  (匹配单个)
    url(r'^page/(?P<id>[0-9]+)$', views.page_view),

    # http://127.0.0.1:8000/20/mul/40   （匹配多个）
    url(r'^(?P<x>\d{1,2})/(?P<op>\w+)/(?P<y>\d{1,2})$', views.cal_view),

    # http://127.0.0.1:8000/formtest/  (get/post)
    url(r'^formtest/$', views.form_view),

]
