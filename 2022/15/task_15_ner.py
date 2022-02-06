def f(x, y, A):
    return ((48 != y + 2*x) or (A < x) or (A < y))


for A in range(300):
    flag = 1
    for x in range(300):
        for y in range(300):
            if f(x, y, A) == 0:
                flag = 0
                break
    if flag:
        print(A)