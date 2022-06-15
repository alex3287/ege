for A in range(100):
    flag = 1
    for x in range(31):
        for y in range(21):
            f = (y + 2*x < A) or (x > 30) or (y > 20)
            if f == 0:
                flag = 0
    if flag:
        print(A)