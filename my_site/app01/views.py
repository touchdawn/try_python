import datetime

from django.shortcuts import render, HttpResponse, redirect
import pymysql
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

# Create your views hereeeeeee.
from app01 import models


def toast(request):
    messages.success(request, "哈哈哈哈")


def test_view(request):
    print("执行业务逻辑计算中")

    return HttpResponse("test_view success")


def runoob(request):
    # context          = {}
    # context['hello'] = 'Hello World!'
    # return render(request, 'runoob.html', context)

    views_name = "菜鸟教程"
    return render(request, "runoob.html", {"name": views_name})


@csrf_exempt
def login(request):
    error_msg = ''
    if request.method == "POST":
        user = request.POST.get('user', None)  # 避免提交空，时异常
        # user = user.strip()  # 用户输入末尾有空格是去空格
        pwd = request.POST.get('pwd', None)
        obj = models.Account.objects.filter(username=user, password=pwd).first()
        # obj = models.Account.objects.get(name=user)

        # obj = models.Account.username.filter(username=user)

        # if user == "root" and pwd == "123":
        if obj:
            print('user=' + user, 'pwd=' + pwd)
            res = redirect("../index")
            res.set_cookie('login_user', user)
            return res
        else:
            error_msg = "账号或者密码不对"
            print(error_msg)
            print('user=', user, 'pwd=', pwd)
    return render(request, 'login.html', {'error_msg': error_msg})


###################################################
@csrf_exempt
def register(request):
    error_msg = ''
    success_msg = ''
    if request.method == "POST":
        user = request.POST.get('user', None)  # 避免提交空，时异常
        # user = user.strip()  # 用户输入末尾有空格是去空格
        pwd = request.POST.get('pwd', None)
        pwd_again = request.POST.get('pwd_again', None)
        email = request.POST.get('email', None)
        obj = models.Account.objects.filter(username=user).first()

        if obj:
            print('XXuser=' + user, 'pwd=' + pwd)
            res = redirect("../login")
            error_msg = '账户已存在！'
            messages.error(request, '账户已存在!')
            # return redirect('../register', {'error_msg': error_msg})
        elif pwd != pwd_again:
            messages.error(request, '两次密码不一致!')
        else:
            models.Account.objects.create(username=user, password=pwd, email=email)
            print('add account success!')
            print('user=', user, 'pwd=', pwd, 'email=', email)
            success_msg = '注册成功！'
            return redirect('../index', {'success_msg': success_msg})
    return render(request, 'register.html', {'error_msg': error_msg, 'success_msg': success_msg})


##########################################


def base(request):
    return render(request, 'base.html')


def index(request):
    login_user = request.COOKIES.get('login_user')
    if not login_user:
        return redirect('../login')
    print(request.GET.items)
    print(models)
    return HttpResponse("welcome ..")


def new_article(request):
    return render(request, 'new_article.html')


def login_view(request):
    # html = """
    #
    # """
    #
    # return HttpResponse(html)
    return render(request, 'form.html')


def article_2003(request):
    return HttpResponse('article 2003')


def article_year(request, year, version):
    version_detail = "1.0.1"
    return HttpResponse('article %s %s %s' % (year, version, version_detail))


def article_detail(request, year, month, slug):
    return HttpResponse('article %s-%s %s' % (year, month, slug))


def article_archive(request, year, month):
    return HttpResponse('article 动态 %s-%s' % (year, month))


def article_archive3(request, arg1, arg2, slug):
    return HttpResponse('article 动态 %s-%s-%s' % (arg1, arg2, slug))


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def detail(request):
    # try:
    #     p = Poll.objects.get(pk=poll_id)
    # except Poll.DoesNotExist:
    #     raise Http404("Poll does not exist")
    context = {}
    context['hello'] = 'Hello World!'
    # return render(request, 'runoob.html', context)
    return render(request, 'try_python/my_site/html/mysheet.html')


def sql_test(request):
    conn = pymysql.connect(host='localhost', port=8889, user='root', passwd='root', db='data_structure')
    cursor = conn.cursor()  # 游标

    cursor.execute("select username, password from user;")

    data = cursor.fetchall()

    return HttpResponse(str(data))

    # conn = pymysql.connect(host='w.rdc.sae.sina.com.cn:3306', port=3306, user='n2o3n3x353', passwd='ijx1j43w5wmk4l1mmz134kzmwx25lw5ywxw3x0h2', db='app_tryprogram')
    # cursor = conn.cursor()  # 游标
    #
    # cursor.execute("select username, password from user;")
    #
    # data = cursor.fetchall()
