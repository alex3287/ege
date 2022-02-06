# вариант столбик
# A = [int(i) for i in open('input.txt')]

# произвольный вариант
with open('input.txt') as fin:
    s = fin.readline()
    A = [int(i) for i in s.split()]

print(A)