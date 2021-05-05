#课堂练习
a = int(input('a:'))
b = int(input('b:'))


def resolve(x, y):
    for i in range(1, a):
        if a % i == 0 and b % i == 0:
            answer = i
    return answer


# resolve(a, b)
print(resolve(a, b))
