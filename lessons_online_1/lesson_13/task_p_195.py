s = open('input.txt').readline()
# print(s)   GAGHFFAHFFB

temp = ''
count = 0
flag = 0
for i in range(len(s)):
    if s[i] == 'A':
        temp = ''
        flag = 1
    if flag == 1:
        temp += s[i]
    if s[i] == 'B':
        if len(temp) >= 20 and temp.count('F') == 2 and temp.count('A') == 1:
            count += 1
        temp = ''
        flag = 0
print(count)