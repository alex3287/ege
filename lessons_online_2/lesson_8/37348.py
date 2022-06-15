# count_pairs
# sum_max
# 7 -> 3, 17, 2, 4, 5
# 3 -> 17, 2, 4, 5
# 17 -> 5
# 2 -> 4, 5
# 4 -> 5

# 13, 24

A = [int(i) for i in open('input.txt')]
# print(A)
count = 0
sum_max = 0
for i in range(len(A)-1):
    for j in range(i+1, len(A)):
        if A[i] * A[j] % 34 != 0:
            count += 1
            if A[i] + A[j] > sum_max:
                sum_max = A[i] + A[j]

print(count, sum_max)