A_even = []
A_odd = []
for i in open('input.txt'):
    temp = int(i)
    if temp % 2 == 0:
        A_even.append(temp)
    else:
        A_odd.append(temp)

maxi = max(max(A_even), max(A_odd))
A = []
for i in A_even:
    for j in A_odd:
        summ = i + j
        if summ <= maxi:
            A.append(summ)

count = 0
sum_max = 0
for i in A:
    if i in A_even or i in A_odd:
        count += 1
        sum_max = max(sum_max, i)
print(count, sum_max)

