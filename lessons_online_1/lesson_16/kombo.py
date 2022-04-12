B = ['А', 'Б', 'В', 'Г']
count = 0
for a in B:
    for b in B:
        for c in B:
            for d in B:
                for e in B:
                    for f in B:
                        temp = a+b+c+d+e+f
                        if temp[0] not in 'А':
                            if 'АА' not in temp and 'ББ' not in temp and 'ВВ' not in temp and 'ГГ' not in temp:
                                count += 1
                                print(temp)

print(count)