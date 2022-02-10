def f(x, a1, a2):
    return ((17 <= x <=58) <= ((not(29 <= x <= 80) and \
                                not(a1 <= x < a2)) <= (not(17 <= x <= 58))))

maxi = 10000
for a1 in range(-100, 100):
    for a2 in range(-100, 100):
        flag = 1
        for x in range(-100, 100):
            if f(x, a1, a2) == 0:
                flag = 0
                break
        if flag:
            if a2 - a1 < maxi:
                maxi = a2 - a1
print(maxi)

