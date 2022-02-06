A = [int(i) for i in open('17-4.txt')]
print(A)

count = 0
mini = 10001

for i in A:
    if (i % 31 == 0 or i % 47 == 0 or i % 53 == 0) and (i % 3 == i % 5):
        count += 1
        if i < mini:
            mini = i

print(count, mini)

