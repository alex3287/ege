def summ_min_max_dev(number):
    summ = 0
    for i in range(2, (int(number**0.5)+1)):
        if number % i == 0:
            summ += i + number // i
            return summ
    return 0


for i in range(800001, 900000):
    summ = summ_min_max_dev(i)
    if summ % 138 == 0 and summ != 0:
        print(i, summ)