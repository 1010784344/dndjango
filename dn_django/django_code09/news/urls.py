# -*- coding: utf-8 -*-


from django.conf.urls import url
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/news/index/
    url(r'^index$', views.index_view),
]
