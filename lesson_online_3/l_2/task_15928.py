def f(a1, a2, x, y):
    return (((a1 <= x <= a2) <= (x*x <= 81) and ((y*y <= 36) <= (a1 <= y <= a2))))

#[4 19]
#[4 30]
maxi = 0
for a1 in range(-50, 100):
    for a2 in range(a1+1, 101):
        flag = 1
        for x in range(-50, 100):
            for y in range(-50, 100):
                if f(a1, a2, x, y) == False:
                    flag == 0
                    break
        if flag and a2-a1 > maxi:
            maxi = a2-a1
print(maxi)