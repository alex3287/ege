with open('input.txt') as fin:
    s = fin.readline()

    count = 0
    count_max = 0

    for i in range(len(s)):
        if (s[i] == 'X' and count%3 == 0) or (s[i] == 'Y' and count % 3 == 1) \
                or (s[i] == 'Z' and count % 3 == 2):
            count += 1
            if count > count_max:
                count_max = count
        elif s[i] == 'X':
            count = 1
        else:
            count = 0
    print(count_max)