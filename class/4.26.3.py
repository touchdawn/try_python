def func_lib():
    def add(x,y):
        return x + y
    return add

fadd = func_lib()
print(fadd(1,2))

# fadd = add()  #   error
# print(fadd(1,2))