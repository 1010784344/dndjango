# -*- coding: utf-8 -*-


from django.http import HttpResponse

POST_FORM = """

<form method="post">
用户名：<input type="text" name="uname">
<input type="submit" value="提交">
</from>

"""


def page_view(request, id):
    str = u'这是编号为%s的网页' % id
    return HttpResponse(str)


def index_view(request):
    str = u'这是我的首页'
    return HttpResponse(str)


def cal_view(request, x, op, y):
    html = 'x:%s, op:%s, y:%s' % (x, op, y)
    return HttpResponse(html)


def form_view(request):
    if request.method == 'GET':
        return HttpResponse(POST_FORM)
    elif request.method == 'POST':
        uname = request.POST.get('uname','root')
    return HttpResponse('uname is %s!' % uname)


def test_view(request):
    # 方案一
    # from django.template import loader
    # t = loader.get_template("test.html")
    # html = t.render()
    # return HttpResponse(html)

    # 方案二(主要使用)
    from django.shortcuts import render
    dic = {
        'username': 'bieke',
        'age': 18
    }

    return render(request, 'test.html', dic)


if __name__ == '__main__':
    print(1)
