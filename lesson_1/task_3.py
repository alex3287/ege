def sum_odd_number(number):
    s = 0
    for i in range(1, number + 1, 2):
        s += i
    return s


# n = 11
print(sum_odd_number(122))