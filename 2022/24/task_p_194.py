with open('input.txt') as fin:
    s = fin.readline()
# print(s)


count = 0
length = 0
n = len(s)
t = 0
flag = 0


# A = []
# t = ''
for i in range(n):
    # if flag:
    #     t += s[i]
    #     current_count += 1
    #     if s[i] == 'F':
    #         count_F = 1
    #     elif s[i] == 'B':
    #         flag = 0
    #         if count_F == 1 and current_count < 16:
    #             count += 1
    #         count_F = 0
    #     elif s[i] == 'A':
    #         flag = 1
    #         count_F = 0
    #         current_count = 1
    # elif s[i] == 'A':
    #     flag = 1
    #     count_F = 0
    #     current_count = 1
    if s[i] == 'A':
        current_count = 1
        j = i+1
        find_F = 0
        while j < n and current_count < 14 and s[j] != 'B':
            if s[j] == 'F':
                find_F = 1
            elif s[j] == 'A':
                break
            j += 1
            current_count += 1

        if find_F and s[j] == 'B':
            count += 1


print(count)