# 6
def f_kon(x, A):
    # return (x & 25 != 0) <= ((x & 19 == 0) <= (x & A != 0))
    return (x & A != 0) <= ((x & 10 == 0) <= (x & 3 != 0))


def f_del(x, A):
    return (A % 45 == 0) and ((750 % x == 0) <= ((A % x != 0) <= (120 % x != 0)))


def f_ner(x, y, A):
    return (y + 2*x != 48) or (A < x) or (x < y)


for A in range(200):
    flag = 1
    for x in range(200):
        for y in range(200):
            if f_ner(x, y, A) == 0:
                flag = 0
                break
    if flag:
        print(A)
