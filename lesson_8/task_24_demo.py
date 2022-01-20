with open('input.txt') as fin:
    s = fin.readline()
    # print(s)

max_count = 0
count = 1
A = []
for i in range(len(s)-1):
    if s[i] + s[i+1] != 'PP':
        count += 1
        if max_count < count:
            max_count = count
    else:
        count = 1
    A.append(count)
print(A)
print(max_count)