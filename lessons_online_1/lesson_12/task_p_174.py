# 3 4 5 -> 9 + 16 = 25

for a in range(1, 5001): # 10
    for b in range(a, 5001):
        for c in range(b, 5001):
            if a*a + b*b == c*c:
                print(a, b, c)