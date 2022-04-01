# Вариант 2 РешуЕГЭ
# 17 2, 17 3, 17 4, 17 12 -> 1 20
# 2 3, 2 4, 2 12 -> 3 14
# 3 4, 3 12 -> 2 15
# 4 12 -> 1 16
# 7 20
A = [int(i) for i in open('input.txt')]
count = 0
sum_max = 0
p = 0

for i in range(len(A)-1):
    for j in range(i+1, len(A)):
        p = A[i] * A[j]
        if p % 34 != 0:
            count += 1
            if A[i] + A[j] > sum_max:
                sum_max = A[i] + A[j]
print(count, sum_max)
