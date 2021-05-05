
def digui(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return digui(n - 1) + digui(n - 2)


n = 100

print('第100位:', digui(n))