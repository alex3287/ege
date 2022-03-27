LETERS = ('О', 'Л', 'Ь', 'Г', 'А')
WAL = ('О', 'А')
s = []
for a in LETERS:
    for b in LETERS:
        for c in LETERS:
            for d in LETERS:
                for e in LETERS:
                    if a != 'Ь':
                        if a in WAL and b != 'Ь' or a not in WAL:
                            if b in WAL and c != 'Ь' or b not in WAL:
                                if c in WAL and d != 'Ь' or c not in WAL:
                                    if d in WAL and e != 'Ь' or d not in WAL:
                                        if len(set(a+b+c+d+e)) == 5:
                                            s.append(a+b+c+d+e)
print(len(s))


