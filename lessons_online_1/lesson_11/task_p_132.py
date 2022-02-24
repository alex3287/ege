# [10 ...
# 12 -> 2, 3, 4, 6
# 16 -> 2, 4, 8 => 3!

def count_dev(number):
    result = 0
    max_dev = 1
    if number**0.5 == int(number**0.5):
        for i in range(2, int(number**0.5)+1):
            if number % i == 0:
                result += 1
                if number // i != i:
                    result += 1
                if number // i > max_dev:
                    max_dev = number // i
            if result > 3:
                return result, max_dev
    return result, max_dev


# print(count_dev(36))
for i in range(247264322, 369757524):
    count, max_dev = count_dev(i)
    if count == 3:
        print(i, max_dev)