DIGITS = '0123456789'

with open('input.txt') as fin:
    s = fin.readline()
    print(s)

count_number = 0
flag = 0
number = ''

for i in range(1, len(s)):
    if s[i] == '7' and s[i-1] not in DIGITS:
        flag = 1
    if flag and s[i] in DIGITS:
        number += s[i]
    if len(number) == 11:
        if int(number[0]) + int(number[1]) == int(number[-2]) + int(number[-1]):
            count_number += 1
            flag = 0
            number = ''
    if s[i] not in DIGITS:
        flag = 0
        number = ''
print(count_number)

