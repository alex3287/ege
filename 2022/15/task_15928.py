# (a1 <= x <= a2) <= (x*x <= 81)
# (y*y <= 36) <= (a1 <= y <= a2)
def f(x, a1, a2):
    # return (a1 <= x <= a2) <= (x*x <= 81)
    return (x*x <= 36) <= (a1 <= x <= a2)
A = []
for a1 in range(-100, 100):
    for a2 in range(a1+1, 101):
        flag = 1
        for x in range(-100, 100):
            if f(x, a1, a2) == 0:
                flag = 0
                break
        if flag:
            A.append(a2 - a1)
print(A)
print(max(A))