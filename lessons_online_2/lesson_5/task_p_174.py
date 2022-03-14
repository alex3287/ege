# 3, 4, 5 => 9 + 16 = 25
# 4, 3, 5 => 16, 9 = 25
# 6, 8, 10
# 5, 12, 13
# 3, 4  sqrt(2)

count = 0
sum_max = 0
c_max = 0
for a in range(1, 5001):
    for b in range(a, 5001):
        c = (a*a + b*b)**0.5
        if c < 5001 and c == int(c):
            count += 1
            if a+b+c > sum_max:
                sum_max = a+b+c
                c_max = int(c)
print(count, c_max)
#125 000 000 000