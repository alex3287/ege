# 11
A = [int(i) for i in open('27-9b.txt')]
A1 = A[:6]
min_odd = 1002
min_odd_p = 1000*1000+1
print(A1)
print(A[6])
for i in range(6, 60000):
    new = A[i]
    if A1[0] % 2 != 0 and A1[0] < min_odd:
        min_odd = A1[0]
    p = min_odd * new
    if p % 2 != 0 and p < min_odd_p:
        min_odd_p = p
    for j in range(5):
        A1[j] = A1[j+1]
    A1[-1] = new
print(min_odd_p)