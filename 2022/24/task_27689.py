s = open('input.txt').readline()
# print(s)

length_max = 0
length = 0
i = 0
while i < len(s)-2:
    temp = s[i:i+3]
    if temp == 'XYZ':
        length += 3
        i += 3
        if length > length_max:
            length_max = length
    elif s[i:i+2] == 'XY' and length > 2:
        length += 2
        if length > length_max:
            length_max = length
        length = 0
    elif s[i] == 'X' and length > 2:
        length += 1
        if length > length_max:
            length_max = length
        length = 0
    else:
        length = 0
        i += 1
print(length_max)