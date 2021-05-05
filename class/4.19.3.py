# c = int(input("a:"))
# d = int(input("b:"))
a = 98
b = 98


def fun(a, b):
    a_yueshu = []
    b_yueshu = []

    for i in range(1, a + 1):
        if a % i == 0:
            a_yueshu.append(i)

    for i in range(1, b + 1):
        if b % i == 0:
            b_yueshu.append(i)

    yueshu = set(a_yueshu) & set(b_yueshu)

    max_yueshu = max(list(yueshu))
    min_yueshu = min(list(yueshu))

    return {"max_yueshu": max_yueshu, 'min_yueshu': min_yueshu}


dict = fun(a, b)

print(dict['max_yueshu'])
