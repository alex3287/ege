
def f(x, y, A):
    return (y + 2 * x < A) or (x > 30) or (y > 20)


for A in range(100):
    flag = 1
    for x in range(100):
        for y in range(100):
            if f(x, y, A) == 0:
                flag = 0
                break
    if flag:
        print(A)
