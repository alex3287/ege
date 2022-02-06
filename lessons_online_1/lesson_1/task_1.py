# сумма чисел от 1 до 10
n = int(input('-> '))
s = 0
# s = n * (n + 1) // 2
# s = 1 + 2 + ... + 10
for i in range(1, n+1):
    s += i # s = s + i

print(s)