# 3421 -> 10

def sum_digits(number):
    summ = 0
    for i in str(number):
        summ += int(i)
    return summ


n = int(input('-> '))
print(sum_digits(n))

