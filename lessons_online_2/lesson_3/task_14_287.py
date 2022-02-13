for x in range(1, 100000):
    temp = 4**1014 - 2**x + 12
    temp = hex(temp)[2:]
    a = temp.count('0')
    if a == 2000:
        print(x)
        break

# print(bin(23)[2:])