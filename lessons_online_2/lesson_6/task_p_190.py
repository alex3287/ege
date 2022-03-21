#16
s = open('input.txt').readline()
# print(s)

count = 0
count_max = 0
dot = 0
for i in s:
    if i in 'AEIOUY':
        count = 0
        dot = 0
    else:
        count += 1
        if i == '.':
            dot += 1
        if count > count_max and dot > 5:
            count_max = count
print(count_max)