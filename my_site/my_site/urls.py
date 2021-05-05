"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, register_converter
from django.conf.urls import include

from . import converters

register_converter(converters.YearConverter, 'yyyy')

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('test',views.test_view),
    # path('login',views.login_view),
    #
    #
    # # 下段已淘汰
    # # re_path(r'^articles/2003/$',views.article_2003),
    # # re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.article_archive),
    # # re_path(r'^articles/(?P<arg1>[0-9]{4})/(?P<arg2>\d+)/(?P<slug>[\w-]+)/$', views.article_archive3)
    # path("articles/2003/", views.article_2003),
    # path("articles/<yyyy:year>/", views.article_year),
    # path("articles/<int:year>/<int:month>/<slug:slug>/", views.article_detail)
    #
    # #上端已淘汰
    path("admin/",admin.site.urls),
    path("app01/", include("app01.urls"))
]
