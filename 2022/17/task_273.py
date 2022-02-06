A = [int(i) for i in open('input.txt')]
# print(A)

maxi = max(A)
count = 0
min_item = 100000
max_item = -100000

for i in range(len(A)-2):
    temp = [A[i], A[i+1], A[i+2]]
    if sum(temp) < maxi:
        count += 1
        min_item = min(min_item, min(temp))
        max_item = max(max_item, max(temp))

print(count, min_item + max_item)
