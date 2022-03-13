# 8 -> 1, 2, 4, 8
# 16 -> 1, 2, 4, 8, 16
# 13 -> 1, 13
# 25 -> 1, 5, 25
# 36 -> 1, 2, 3, 4, 6, 6, 9, 12, 18, 36

def devision_numbers(number):
    A = []
    for i in range(1, number+1):
        if number % i == 0:
            A.append(i)
    return A


print(devision_numbers(8))
for i in range(338472, 338495):
    A = devision_numbers(i)
    if len(A) == 4:
        print(i, '->', A)