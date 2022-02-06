# сумма 1 до N
# 10 -> 55

def sum_numbers(number):
    summ = 0
    for i in range(number+1):
        summ += i
    return summ


n = int(input('-> '))
print(sum_numbers(n))