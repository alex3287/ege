A = [int(i) for i in open('input.txt')]
print(A)

count = 0
max_sum = 0

for i in range(len(A)-1):
    if A[i] % 3 == 0 or A[i+1] % 3 == 0:
        count += 1
        if max_sum < A[i] + A[i+1]:
            max_sum = A[i] + A[i+1]

print(count, max_sum)