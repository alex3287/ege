S = ['Ш', 'К', 'О', 'Л', 'А']
count = 0
for a in S:
    for b in S:
        for c in S:
            temp = a+b+c
            if temp.count('К') == 1:
                count += 1
print(count)