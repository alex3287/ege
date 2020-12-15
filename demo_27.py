def findNumber(A):
    mini = 100000
    sum = 0
    for i in A:
        sum += max(i)
        temp = max(i) - min(i)
        if temp % 3 != 0 and temp < mini:
            mini = temp
    if sum % 3 != 0:
        return sum
    return sum - mini


A = [[int(j) for j in i.split()] for i in open('27-A.txt') if ' ' in i]
B = [[int(j) for j in i.split()] for i in open('27-B.txt') if ' ' in i]

print(findNumber(A))
print(findNumber(B))