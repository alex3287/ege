# 12 -> 2+6 = 8
# 25 -> 5+5 = 10
# 17 -> 0 = 0

def sum_min_max_dev(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return i + number // i
    return 0


# print(sum_min_max_dev(12))
for i in range(700000, 800000):
    M = sum_min_max_dev(i)
    if M % 10 == 8:
        print(i, M)
