def sum_digits(number):
    s = 0
    for i in str(number):
        s += int(i)
    return s


A = [int(i) for i in open('input.txt')]
print(A)

count = 0
min_sum = 100000
sum_35 = 0

for i in A:
    if i % 35 == 0:
        sum_35 += sum_digits(i)
print(sum_35)
for i in range(len(A)-1):
    if (A[i] > sum_35 and (A[i+1] < sum_35 and A[i+1] % 256 == 239)) or (A[i + 1] > sum_35 and (A[i] < sum_35 and A[i] % 256 == 239)):
        count += 1
        if A[i] + A[i+1] < min_sum:
            min_sum = A[i] + A[i+1]

print(count, min_sum)