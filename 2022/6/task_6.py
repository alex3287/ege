for i in range(1, 1000):
    d = i
    n = 5
    s = 83
    while s <= 1200:
        s = s + d
        n = n + 6
    if n == 89:
        print(i, n)