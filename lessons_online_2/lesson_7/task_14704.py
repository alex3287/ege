
def f(x, y, A):
    return ((x < 6) <= (x*x < A)) and ((y*y <= A) <= (y <= 6))

k = 0
for A in range(200):
    flag = 1
    for x in range(200):
        for y in range(200):
            if f(x, y, A) == 0:
                flag = 0
                break
    if flag:
        k += 1
        print(k, A)
