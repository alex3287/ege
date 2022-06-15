A = [int(i) for i in open('input.txt')]

count = 0
sum_max = 0

for i in range(len(A)-1):
    sum = A[i] + A[i+1]
    if (A[i] % 3 == 0 or A[i+1] % 3 == 0) and sum % 5 == 0:
        count += 1
        if sum > sum_max:
            sum_max = sum

print(count, sum_max)