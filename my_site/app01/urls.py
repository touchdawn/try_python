
from django.urls import path, include
from app01 import views

extra_urls = [
    #path("<yyyy:year>/", views.article_year),
    path("<int:year>/<int:month>/<slug:slug>/", views.article_detail)
]

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
    path("articles/<yyyy:year>/", views.article_year, {'version': 'v1.0'}),
    path("articles/", include(extra_urls)),
    path("sql_test", views.sql_test),
    path("time", views.current_datetime),
    path("html", views.detail),
    path('runoob/', views.runoob),
    path('login/', views.login),
    path('index/', views.index),
    path('base/', views.base),
    path('register/', views.register),
    path('new_article/', views.new_article),
]
