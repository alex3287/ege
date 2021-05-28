import heapq
A = {}
# with open('test.txt') as fin:
for i in open('test.txt'):
    k, d = map(int, i.split())
    A[d] = k
print(A)
A2 = sorted(A)
print(A2)
