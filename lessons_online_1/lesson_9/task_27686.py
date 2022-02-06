# Текстовый файл  X, Y и Z. Определите длину самой длинной последовательности,
# состоящей из символов X. Хотя бы один символ X находится в последовательности.
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать
# с помощью данного алгоритма.

with open('input.txt') as fin:
    s = fin.
    print(s)

count = 0
count_max = 0
for i in range(len(s)):
    if s[i] == 'X':
        count += 1
        if count > count_max:
            count_max = count
    else:
        count = 0


print(count, count_max)