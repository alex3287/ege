# Текстовый файл состоит из символов L, D и R.
# Определите максимальное количество идущих подряд символов,
# среди которых каждые два соседних различны.
with open('24.txt') as fin:
    s = fin.readline()

    count = 1
    count_max = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        count += 1
        if count > count_max:
            count_max = count
    else:
        count = 1
print(count_max)