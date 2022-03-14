def is_three_dev(number):
    count = 1 if number % 2 == 0 else 0
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            if i % 2 == 0:
                count += 1
            if number // i != i and number // i % 2 == 0:
                count += 1
        if count > 3:
            return False
    return count == 3


for i in range(101000000, 102000001):
    if is_three_dev(i):
        print(i)

