from random import randint as rnd


def sum_negative_item(A):
    summ = 0
    for i in A:
        if i < 0:
            summ += i
    return summ


def max_negative(A):
    for i in A:
        if i < 0:
            maxi = i
            break
    for i in A:
        if i < 0 and i > maxi:
            maxi = i
    return maxi


A = [rnd(-10, 10) for i in range(10)]
print(A)
print(max_negative(A))
