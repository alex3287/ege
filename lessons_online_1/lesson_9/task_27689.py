with open('input.txt') as fin:
    s = fin.readline()
    print(s)

    count = 0
    count_max = 0
    step = 0

    i = 0
    while i < len(s)-2:
        temp = s[i] + s[i+1] + s[i+2]
        if temp == 'XYZ':
            count += 3
            i += 3
            if count > count_max:
                count_max = count
        else:
            count = 0
            i += 1
    string = 'XYZ' * (count_max // 3)
    print(string)
    index = s.find(string) + len(string)
    if index < len(s) and s[index] == 'X':
        count_max += 1
        if index + 1 < len(s) and s[index+1] == 'Y':
            count_max += 1
    # for i in range(len(s)-2):
    #     if step > 0:
    #         step -= 1
    #         continue
    #     temp = s[i] + s[i+1] + s[i+2]
    #     if temp == 'XYZ':
    #         count += 3
    #         step = 2
    #         if count > count_max:
    #             count_max = count
    #     else:
    #         count = 0

print(count, count_max, index)