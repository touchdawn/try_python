# def stu_register(name, age, *apple):
#     print(name, age, apple)
#
#
# stu_register('alex', 22)
# stu_register('jack', 32, 'CN', 'Python')
# # 非固定参数传参
# stu_register('Jack', 32, *['CN', 'Python', 'lol'])
#

def stu_register(name, age, *args, **kwargs):
    print(name, age, args, kwargs)


stu_register('jack', 32, 'CN', 'Python')
# 非固定参数传参
stu_register('Jack', 32, 'CN', 'Python', gender='Male', province="shandong")

