def f(x, y, A):
    return (4*x + 3*y < A) or (x >= y) or (y >= 13)


for A in range(100):
    flag = 1
    for x in range(100):
        for y in range(100):
            if f(x, y, A) == 0:
                flag = 0
                break
    if flag:
        print(A)