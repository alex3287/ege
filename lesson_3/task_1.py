# with open('input.txt') as fin:
#     n = int(fin.readline())
#     A = []
#     for i in range(n):
#         A.append(int(fin.readline()))

# with open('input.txt') as fin:
#     A = [int(i) for i in fin.readlines()]
#     A = A[1:]

A = [int(i) for i in open('input.txt')]
A = A[1:]

print(A)