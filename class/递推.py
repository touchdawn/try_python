#第一项到100


x = [0] * 100
x[:2] = [1] * 2
for i in range(2, 100):
    x[i] = x[i - 1] + x[i - 2]
print('第100位:', x[99])


