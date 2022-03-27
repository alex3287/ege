for i in range(201, 220):
    s = '1' * i
    count = 0
    while '1111' in s:
        s = s.replace('1111', '22', 1)
        s = s.replace('222', '1')
    print(i, '->', s.count('1'))
