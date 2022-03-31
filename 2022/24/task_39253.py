s = open('input.txt').readline()

count = 0
count_temp = 0
count_max = 0
count_D = 0

for i in s:
    if i == 'D':
        count_D += 1
    if count_D == 2:
        count_D = 1
        count = count_temp
        count_temp = 1
        continue
    if count_D == 1:
        count_temp += 1
    count += 1
    if count > count_max:
        count_max = count

print(count_max)

