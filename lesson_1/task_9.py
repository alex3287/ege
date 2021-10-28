from random import randint as rnd


# A = []
# for i in range(10):
#     A.append(rnd(-10, 10))

A = [rnd(-10, 10) for i in range(10)]
print(A)

count_positive = 0
count_negative = 0
mult = 1
s = 0
for i in A:
    if i > 0:
        count_positive += 1
        s += i
    elif i < 0:
        count_negative += 1
        mult *= i
print(count_positive, s)
print(count_negative, mult)
