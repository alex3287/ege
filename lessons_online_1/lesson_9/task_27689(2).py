with open('input.txt') as fin:
    s = fin.readline()
    print(s)

    count = 0
    count_max = 0
    template = 'XYZ'

    while template in s:
        template += 'XYZ'
    template = template[:-3]
    count_max = len(template)

    index = s.find(template) + len(template)
    if index < len(s) and s[index] == 'X':
        count_max += 1
        if index +1 < len(s) and s[index + 1] == 'Y':
            count_max += 1
    print(template, count_max)