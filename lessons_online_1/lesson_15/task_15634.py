# Вариант 2 РешуЕГЭ
def f(y, x, A):
    return (y + 2*x < A) or (x > 30) or (y > 20)


for A in range(0, 100):
    flag = 1
    for x in range(0, 100):
        for y in range(0, 100):
            if f(y, x, A) == 0:
                flag = 0
                break
    if flag == 1:
        print(A)