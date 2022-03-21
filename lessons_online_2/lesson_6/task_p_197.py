def check(string):
    if string == 'ZXY' or string == 'ZYX':
        return True
    return False


s = open('input.txt').readline()
print(s)

count = 0
count_max = 0
i = 0
while i < len(s)-2:
    temp = s[i:i+3]
    if check(temp):
        count += 1
        if count > count_max:
            count_max = count
        i += 3
    else:
        count = 0
        i += 1

print(count_max)