A = [int(i) for i in open('input.txt')]
# print(A)

# 30
# 3 94


def sum_digits(number):
    s = 0
    while number:
        s += number % 10
        number //= 10
    return s


count = 0
min_sum = 100000
sum_49 = 0
for i in A:
    if i % 49 == 0:
        sum_49 += sum_digits(i)

for i in range(len(A)-1):
    if (A[i] > sum_49 and A[i+1] % 10 == 7 and A[i+1] <= sum_49) or \
            (A[i+1] > sum_49 and A[i] % 10 == 7 and A[i] <= sum_49):
        count += 1
        if A[i] + A[i+1] < min_sum:
            min_sum = A[i] + A[i+1]

print(count, min_sum)