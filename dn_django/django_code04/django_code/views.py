# -*- coding: utf-8 -*-


from django.http import HttpResponse

POST_FORM = """

<form method="post">
用户名：<input type="text" name="uname">
<input type="submit" value="提交">
</from>

"""


def say_hi():
    return 'hello world'


class DogName(object):

    def my_dog(self):
        return 'wangwang'


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


def dic_test_view(request):
    from django.shortcuts import render
    dic = {}
    dic['int'] = 88
    dic['str'] = 'xingfu'
    dic['lst'] = ['a', 'b', 'c']
    dic['dict'] = {'a': 9, 'b': 8}
    dic['func'] = say_hi
    dic['class_obk'] = DogName()

    return render(request, 'diffdata.html', dic)


def test_iffor_view(request):
    from django.shortcuts import render
    dic = {}
    dic['age'] = 10

    dic['lst'] = ['tom', 'lily', 'kev']

    return render(request, 'testiffor.html', dic)


def mycal_view(request):
    from django.shortcuts import render
    if request.method == 'GET':

        # 模板这块，如果你调用的这个变量不存在他是不报错的，什么时候有值，他就显示
        # 没值他就是空,所以这里我们不用在进行get请求的时候，赋空值
        # dic = {}
        # dic['res'] = ''
        # dic['x'] = ''
        # dic['y'] = ''
        return render(request, 'mycal.html')
    elif request.method == 'POST':
        dic = {}
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        op = request.POST['op']
        if op == 'add':
            dic['res'] = x + y
        elif op == 'sub':
            dic['res'] = x - y
        elif op == 'mul':
            dic['res'] = x * y
        elif op == 'div':
            dic['res'] = x / y
        dic['x'] = x
        dic['y'] = y
        dic['op'] = op

        return render(request, 'mycal.html', dic)


if __name__ == '__main__':
    print(1)
