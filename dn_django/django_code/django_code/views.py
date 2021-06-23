# -*- coding: utf-8 -*-


from django.http import HttpResponse


def page_view(request, id):
    str = u'这是编号为%s的网页'% id
    return HttpResponse(str)


def index_view(request):
    str = u'这是我的首页'
    return HttpResponse(str)



if __name__ == '__main__':
    print 1