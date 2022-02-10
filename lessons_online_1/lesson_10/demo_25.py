# 12 -> M = 2+6 = 8
# 25 -> M = 5+5 = 10
# 17 -> M = 0
# 36 -> 2, 3, 4, 6, 9, 12, 18
# 25 -> 5
# 47 -> 0

def sum_max_min_dev(number):
    summ = 0
    for i in range(2, (int(number**0.5)+1)):
        if number % i == 0:
            summ += i
            summ += number // i
            return summ
    return 0


# print(sum_max_min_dev(17))
for i in range(700001, 800000):
    M = sum_max_min_dev(i)
    if M % 10 == 8:
        print(i, M)