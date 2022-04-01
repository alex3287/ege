# Вариант 2 РешуЕГЭ
numbers = ('1', '2', '3', '4', '5')
s = []
for a in numbers:
    for b in numbers:
        for c in numbers:
            for d in numbers:
                for e in numbers:
                    temp = a+b+c+d+e
                    if temp.count('1') == 3:
                        s.append(temp)
print(len(s))