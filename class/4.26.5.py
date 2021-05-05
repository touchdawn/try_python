# import math
# from os.path import dirname
# print(dirname('/4.19.1.py'))
import types


class XIAOGUAI:
    def __init__(self, name):
        self.name = name
        self.bloodamount = 99
        self.__marragestatus = False

    def infor(self):
        print('I am a XIAOGUAI! My name is ' + self.name)

    def rumarried(self):
        print(self.__marragestatus)
def attack(self, xiaoguai):
    xiaoguai.bloodamount = xiaoguai.bloodamount - 10
    print('yaha!')


def attacked(xiaoguai):
    xiaoguai.bloodamount = xiaoguai.bloodamount - 10
    print('hoops!')


xg1 = XIAOGUAI('xg1')
xg2 = XIAOGUAI('xg2')
xg3 = XIAOGUAI('xg3')

xg3.attacked = types.MethodType(attacked, xg3)  # 成员中添加函数
xg3.attack = types.MethodType(attack, xg3)  # 成员中添加函数

xg1.infor()
xg2.infor()

# xg3.bloodamount = 99
# xg2.bloodamount = 50
print('My name is ' + xg3.name + ', my blood:' + str(xg3.bloodamount))

# print(isinstance(xg1, XIAOGUAI))
xg3.attacked()

print('My name is ' + xg3.name + ', my blood:' + str(xg3.bloodamount))
xg3.attack(xg2)
print('My name is ' + xg2.name + ', my blood:' + str(xg2.bloodamount))

#print(xg2._XIAOGUAI__marragestatus)  # 访问私有成员,不建议
xg3.rumarried()

