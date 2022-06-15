LETTERS = '.', '-'
s = []
for a in LETTERS:
    for b in LETTERS:
        for c in LETTERS:
            for d in LETTERS:
                s.append(a+b+c+d)
print(len(s))
