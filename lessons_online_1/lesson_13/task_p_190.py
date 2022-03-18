s = open('input.txt').readline()
print(s)
W = 'AEIOUY'

count = 0
count_max = 0
dot = 0
for i in range(len(s)):
    if s[i] not in W:
        if s[i] == '.':
            dot += 1
        count += 1
        if count > count_max and dot > 5:
            count_max = count
    else:
        count = 0
        dot = 0

print(count_max)