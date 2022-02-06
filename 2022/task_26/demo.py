s = 8200  #120
n = 970  #7
A = [int(i) for i in open('26.txt')]

# print(A)

A.sort()
print(A)

summa = 0
count = 0
for i in A:
    if summa + i > s:
        break
    summa += i
    count += 1

# while summa + A[count] <= s:
#     summa += A[count]
#     count += 1

print('count', count)

maxi = A[count-1]
summa -= maxi
for i in range(count, n):
    if summa + A[i] <= s:
        maxi = A[i]
    else:
        break
print(maxi)
# 40 40 40 43 50 70 80 90 90