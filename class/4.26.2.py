# def fun():
#     x = 3
#     count = 2
#     while count > 0:
#         print(x)
#         count = count - 1
# fun()

name = 'alex'
def change_name():
   global name
   name = 'alexxx'
   print(name)

change_name()
print(name)
