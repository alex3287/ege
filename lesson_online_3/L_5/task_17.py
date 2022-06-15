S = [int(i) for i in open('17.txt')]
print(S)
count = 0
summ = 0
for i in S:
    if i % 2 == 0:
        count += 1
        summ += i
Sr = summ/count

k = 0
sum_max = 0
for i in range(len(S) - 1):
    if (S[i] % 3 == 0 or S[i+1] % 3 == 0) and (S[i] < Sr or S[i+1] < Sr):
        k += 1
        if S[i] + S[i+1] > sum_max:
            sum_max = S[i] + S[i+1]

print(sum_max, k)