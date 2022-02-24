# [10, 2000]
# 10 -> 1, 2, 5, 10 => 4
# 12 -> 6
# 24 -> 8
# 36 -> 1, 2, 3, 4, 6, 9, 12, 18, 36 => 9
# 48 -> 1, 2, 3, 4, 6, 8, 12, 16, 24, 48 => 10

def count_dev(number):
    result = 0
    for i in range(1, int(number**0.5)+1):
        if number % i == 0:
            result += 1
            if number // i != i:
                result += 1
    return result


# print(count_dev(36))
count_old = 0
for i in range(700000, 900000):
    count = count_dev(i)
    if count > count_old:
        print(i, count)
        count_old = count