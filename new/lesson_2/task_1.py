A = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 2, 34, 34]
print(A)
B = set(A)
print(B)
for i in B:
    if A.count(i) == 1:
        print(i)
        break
