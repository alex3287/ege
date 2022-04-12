def f(s, f):
    if s > f or s == 14:
        return 0
    if s == f:
        return 1
    return f(s+1, f) + f(s+2, f)


print(f(2, 9))