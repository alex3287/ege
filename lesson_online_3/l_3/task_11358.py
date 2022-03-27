def f(start, finish):
    if start > finish or start == 29:
        return 0
    if start == finish:
        return 1
    return f(start+1, finish) + f(start*2, finish) + f(start*3, finish)


print(f(2, 13) * f(13, 44))