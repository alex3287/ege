# 12 -> 2, 3, 4, 6 = 13
# x -> 6 8 5 5 = 32
# 18 -> 2, 9, 3, 6
# 17 = 0
# 36 -> 2, 3, 4, 6, 9, 12, 18 [2, 18, 3, 12, 4, 9]
def check(number):
    s = str(number)
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True


def sum_max3_dev(number):
    summ = 0
    count = 0
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            temp = i
            summ += number // i
            count += 1
            if count == 3:
                return summ
    if count == 2:
        return summ + temp
    return 0


# def sum_max3_dev(number):
#     A = []
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             A.append(i)
#             A.append(number//i)
#     A.sort()
#     if len(A) > 2:
#         return A[-1] + A[-2] + A[-3]
#     return 0


count = 0
for i in range(10000000, 11000000):
    M = sum_max3_dev(i)
    if M > 0 and check(M):
        print(i, M)
        count += 1
        if count == 5:
            break