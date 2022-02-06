#13364
#34535
#34539
def f(x, a1, a2):
    # return (130 <= x <= 171) <= (((150 <= x <= 185) and \
    #                               not(a1 <= x <= a2)) <= (not(130 <= x <= 171)))
    # return ((a1 <= x < a2) or (10 <= x <= 40)) or ((5 <= x <= 15) <= (35 <= x <= 50))
    return not (not (a1 <= x < a2) and (22 <= x <= 72)) or (42 <= x <= 102)

maxi = 10000
for a1 in range(-20, 300):
    for a2 in range(-20, 300):
        flag = 1
        for x in range(-20, 300):
            if f(x, a1, a2) == 0:
                flag = 0
                break
        if flag:
            if a2 - a1 < maxi:
                maxi = a2 - a1
print(maxi)