# 10 11 12 13 14 15 16 17 18 19 20
# [11 13 17 19 23 29]

# 17 -> 4
# 47 -> 6 - 7
# 36 -> 2, 3, 4, 6, 6, 9, 12, 18

def isprime(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

# 38048 9999972.0
count = 0
A = []
for i in range(3000000, 10000000):
# for i in range(10, 100):
    if isprime(i):
        A.append(i)

print(A)
summa = 0
for i in range(len(A)-1):
    if A[i+1] - A[i] == 2:
        count += 1
        summa = A[i] + A[i+1]

print(count, summa/2)