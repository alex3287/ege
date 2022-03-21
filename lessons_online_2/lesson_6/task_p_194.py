s = open('input.txt').readline()
# print(s)

count = 0
temp = ''
for i in s:
    if i == 'A':
        temp = i
    elif i == 'B':
        temp += i
        if temp[0] == 'A' and len(temp) <= 15:
            if 'F' in temp:
                count += 1
        temp = ''
    else:
        temp += i

print(count)