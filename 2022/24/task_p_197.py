with open('input.txt') as fin:
    s = fin.readline()
print(s)


count = 0
count_max = 0
step = 0
for i in range(len(s)-2):
    if step:
        step -= 1
        continue
    if s[i] + s[i+1] + s[i+2] == 'ZXY' or s[i] + s[i+1] + s[i+2] == 'ZYX':
        step = 2
        count += 1
        if count > count_max:
            count_max = count
    else:
        count = 0
print(count_max)