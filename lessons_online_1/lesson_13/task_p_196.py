s = open('input.txt').readline()
print(s)

count = 0
count_max = 0
i = 0
while i < len(s)-1:
    temp = s[i] + s[i+1]
    if temp == 'ZX' or temp == 'ZY':
        count += 1
        i += 2
        if count > count_max:
            count_max = count
    else:
        count = 0
        i += 1

print(count_max)