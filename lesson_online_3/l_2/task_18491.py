# 0 - Ь
# 1 - Л
# 2 - О
# 3 - Г
# 4 - А
# ОЛАГЬ 01432
# 1_2
count = 0

for i in range(10000, 44444):
    s = str(i)
    if s.count('1') == 1 and s.count('0') == 1 and s.count('2') == 1 and s.count('3') == 1 and s.count('4') == 1:
        w_1 = s.find('2')
        w_2 = s.find('4')
        if w_1 < 4 and s[w_1+1] != '0' or w_1 == 4:
            if w_2 < 4 and s[w_2 + 1] != '0' or w_2 == 4:
                count += 1
print(count)