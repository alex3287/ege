A = [int(i) for i in open('26.txt') if ' ' not in i]
A.sort()
s = k = 0
while s < 8200 and k < 970:
    s += A[k]
    k += 1
s -= A[k-1] + A[k-2]
maxi = 0
for i in range(k-2, len(A)):
    if s + A[i] > 8200:
        break
    if maxi < A[i]:
        maxi = A[i]
print(k-1, maxi)