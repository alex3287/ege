def f(x, A):
    return (x % A != 0) <= ((x % 6 == 0) <= (x % 9 != 0))


for A in range(1, 1000):
    for x in range(1, 1000):
        if f(x, A) == 0:
            break
    else:
        print(A)