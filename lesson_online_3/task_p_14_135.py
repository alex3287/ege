for x in range(10000):
    if hex(x)[-1] == 'a' and len(hex(x)[2:])==2 and len(oct(x)[2:]) == 3:
        print(x, hex(x), oct(x))