from django.contrib import admin
from app01 import models
# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'signature')
    search_fields = ('username', 'email')
    list_filter = ('email',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'account')
    list_filter = ('account', 'pub_date')
    #fields = ('title', 'content')


admin.site.register(models.Account, AccountAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Tag)