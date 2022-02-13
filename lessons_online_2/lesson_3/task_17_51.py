count = 0
maxi = 0
for i in range(117649, 823543):
    if i % 4096 == 174 and i % 8 != 3 and i % 12 != 5:
        count += 1
        # if i > maxi:
        maxi = i
print(count, maxi)

# fae
# x = 1234 -> x % 100
print(int('fae', 16))
print(16**3)
