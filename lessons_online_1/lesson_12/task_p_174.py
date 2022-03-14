count = 0
temp_max = 0
c_max = 0
for a in range(1, 5001):
    for b in range(a, 5001):
        temp = a*a + b*b
        c = int(temp**0.5)
        if c < 5001 and temp == c*c:
            count += 1
            if a+b+c > temp_max:
                temp_max = a+b+c
                c_max = c

print(count, c_max)

