from django.db import models

# Create your models here.


class UserInfo_test(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    age = models.IntegerField()


class Account(models.Model):
    """账户表"""
    username = models.CharField(max_length=64, unique=True)
    email = models.EmailField(unique=True)
    password  = models.CharField(max_length=255)
    register_date = models.DateTimeField(auto_now_add=True)
    signature = models.CharField("签名", max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username


class Article(models.Model):
    """文章表"""

    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    account = models.ForeignKey("Account", on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag", null=True, blank=True)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Tag(models.Model):
    """标签"""
    name = models.CharField(max_length=64, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
