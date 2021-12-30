with open('k8.txt') as fin:
    s = fin.read()
current = maxi = 1
mas = [s[0]]
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        current += 1
        if current == maxi:
            mas.append(s[i])
        elif maxi < current:
            maxi = current
            mas = [s[i]]
    else:
        current = 1

for i in mas:
    print(i, maxi)