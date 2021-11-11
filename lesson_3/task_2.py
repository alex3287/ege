with open('input_2.txt') as fin:
    # A = list(map(int, fin.readline().split()))
    A = fin.readline().split()
    A = [int(i) for i in A]

print(A)