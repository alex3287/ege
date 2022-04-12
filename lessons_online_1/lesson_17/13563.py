count = 0
for i in range(1000, 10000):
    # x1 = i // 1000
    # x2 = i // 100 % 10
    # x3 = i // 10 % 10
    # x4 = i % 10
    s = str(i)
    x1 = int(s[0])
    x2 = int(s[1])
    x3 = int(s[2])
    x4 = int(s[3])
    if x1 % 2 != 0 and x2 % 2 != 0 and x3 % 2 != 0 and x4 % 2 != 0:
        s1 = x1 + x2
        s2 = x3 + x4
        if s1 > s2:
            num = str(s2) + str(s1)
        else:
            num = str(s1) + str(s2)
        if num == '616':
            count += 1
            print(count, i, num)