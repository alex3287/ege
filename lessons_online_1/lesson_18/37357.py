# 6 -> 6 + 2; 6 + 10
# 4 -> 4 + 12
# 2 ->
# 10

A = [int(i) for i in open('input.txt')]
# print(A)
sum_max = 0
count = 0

for i in range(len(A)-1):
    for j in range(i+1, len(A)):
        temp = A[i] + A[j]
        if temp % 8 == 0:
            count += 1
            if temp > sum_max:
                sum_max = temp

print(count, sum_max)