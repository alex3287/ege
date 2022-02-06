def f(x, A):
    return (x & 25 != 0) <= ((x & 17 == 0) <= (x & A != 0))


for A in range(1000):
    for x in range(1000):
        if f(x, A) == 0:
            break
    else:
        print(A)

