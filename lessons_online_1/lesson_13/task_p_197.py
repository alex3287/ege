s = open('input.txt').readline()
print(s)

count = 0
count_max = 0
i = 0
while i < len(s)-2:
    temp = s[i] + s[i + 1] + s[i + 2]
    if temp == 'ZXY' or temp == 'ZYX':
        count += 1
        i += 3
        if count > count_max:
            count_max = count
    else:
        count = 0
        i += 1

print(count_max)
# for i in range(len(s)-2):
#     temp = s[i]+s[i+1]+s[i+2]
#     if temp == 'ZXY' or temp == 'ZYX':
#         count += 1
#         if count > count_max:
#             count_max = count
#     else:
#         count = 0