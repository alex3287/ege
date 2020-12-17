A = [int(i) for i in open('27-9b.txt')]
N = A.pop(0)
B = A[:6]
minP = 1000001
mini = 1001
print(A)
print(B)
print(N)

for i in range(6, N):
    if mini > B[0] and B[0] % 2 != 0:
        mini = B[0]
    tempP = A[i] * mini
    if tempP < minP and tempP % 2 != 0:
        minP = tempP
    for j in range(5):
        B[j] = B[j+1]
    B[5] = A[i]

if minP != 1000001:
    print(minP)
else:
    print(-1)