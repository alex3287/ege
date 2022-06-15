x = 5  # 101 -> 10; 101 <- 1010; ________
x = 191
x = x >> 1
# print(bin(191))
x = x >> 1
x += 4
x = x >> 1
x = x >> 1
x += 4
print(x)
print(bin(x))