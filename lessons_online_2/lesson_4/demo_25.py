# 12 -> 2+6 = 8
# 25 -> 5+5 = 10
# 17 -> 0
# 36 -> 2, 3, 4, 6, 9, 12, 18

def sum_min_max_dev(number):
    for i in range(2, (int(number**0.5)+1)):
        if number % i == 0:
            return i + number // i
    return 0


# print(sum_min_max_dev(5678765431))

count = 0
for i in range(700000, 800000):
    M = sum_min_max_dev(i)
    if M % 10 == 8:
        count += 1
        print(i, M)
        # if count == 5:
        #     break