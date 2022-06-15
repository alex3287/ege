x = 4**2020 + 2**2017 - 15

count = 0
while x > 0:
    d = x % 2
    if d == 1:
        count += 1
    x //= 2

print(count)