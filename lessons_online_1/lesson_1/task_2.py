# s = 1 + 3 + 5 + 7 + 9
# 1 2 3 4 5 6 7 8 9
n = int(input('-> '))
s = 0
for i in range(1, n+1, 2):
    s += i
    # if i % 2 != 0:
    #     s += i
print(s)