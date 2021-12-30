A = [int(i) for i in open('26-J1.txt')]
A.sort()
k = 0
while len(A) > 1:
    temp = A.pop()
    for i, item in enumerate(A):
        if item + temp == 100:
            k += 1
            del A[i]
            break
        if item + temp > 100:
            break
print(k)