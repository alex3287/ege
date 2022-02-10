def check_three_dev(number):
    mini = 10000000
    dev_3 = 0
    for i in range(100, 1000):
        if number % i == 0:
            if i % 10 == 3:
                dev_3 += 1
                if i < mini:
                    mini = i
    if dev_3 == 3:  # fixme
        return mini
    return 0
# print(check_three_dev(912912))

for i in range(912674, 1000000):
    temp = check_three_dev(i)
    if temp % 10 == 3:
        print(i, temp)