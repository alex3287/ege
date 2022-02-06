# 3456 -> 18 => 3 + 4 + 5 + 6
# 24 -> 6
# 7 -> 7


def sum_digits_number(number):
    s = str(number)
    summa = 0
    for i in s:
        summa += int(i)
    return summa


def sum_digits_number_2(number):
    summa = 0
    while number > 0:
        digit = number % 10
        summa += digit
        number //= 10
    return summa


n = int(input('-> '))
print(sum_digits_number_2(n))