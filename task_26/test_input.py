s = 8200
n = 970

with open('input.txt') as fin:
    A = [int(i) for i in fin.readline().split()]

# print(A)
with open('otput.txt', 'w') as fout:
    for i in A:
        print(i, file=fout)