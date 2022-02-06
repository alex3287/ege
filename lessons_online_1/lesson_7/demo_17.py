A = [int(i) for i in open('input.txt')]
# print(A)

count = 0
sum_max = -20001

for i in range(len(A)-1):
    if A[i] % 3 == 0 or A[i+1] % 3 == 0:
        count += 1
        if A[i] + A[i+1] > sum_max:
            sum_max = A[i] + A[i+1]

print(count, sum_max)