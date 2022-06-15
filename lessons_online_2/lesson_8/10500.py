D = ['1', '2', '3', '4', '5']
count = 0

for a in D:
    for b in D:
        for c in D:
            for d in D:
                for e in D:
                    temp = a+b+c+d+e
                    if temp.count('1') == 3:
                        count += 1

print(count)
