with open('input.txt') as fin:
    s = fin.readline()
print(s)

count = 1
count_max = 0
for i in range(len(s)-1):
    if s[i] + s[i+1] != 'PP':
        count += 1
        if count > count_max:
            count_max = count
    else:
        count = 1
print(count_max)
