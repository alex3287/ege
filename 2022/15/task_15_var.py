#7763
#34544
def f(x, a1, a2):
    # return (((5 <= x <= 30) == (14 <= x <= 23))<= (not(a1 <= x < a2)))
    return ((10 <= x <= 39) and (23 <= x <= 58)) <= ((23 <= x <= 58) and (a1 <= x <= a2))
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