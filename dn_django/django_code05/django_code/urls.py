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


    # http://127.0.0.1:8000/templatetest/  (模板层测试)
    url(r'^templatetest/$', views.test_view),

    # http://127.0.0.1:8000/difdata/  (模板层渲染不同类型的数据)
    url(r'^difdata/$', views.dic_test_view),

    # http://127.0.0.1:8000/testiffor/  (模板层if 标签)
    url(r'^testiffor/$', views.test_iffor_view),

    # http://127.0.0.1:8000/mycal/  (模板练习加法)
    url(r'^mycal/$', views.mycal_view, name='cal_add'),

    # http://127.0.0.1:8000/testurl/  (相对路由)
    url(r'^testurl/$', views.test_url_view, name='test_url'),

    # http://127.0.0.1:8000/myurl/  (相对路由)
    url(r'^myurl/$', views.test_syn_view, name='my_url'),

]
