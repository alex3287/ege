# 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12, 13, 14, 15, 16, 17, 18, 19, 20
# 3, 5, 7, 11, 13, 17, 19, 23, 29
# 25 -> 5
# 36 -> 2, 3, 4, 6, 9, 12, 18
# 37 -> 2, 3, 4, 5, 6
# 400 -> 2, 4, 20, 20, 100, 200

def issimple(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True


# A = []
# for i in range(3000000, 10000001):
#     if issimple(i):
#         A.append(i)
A = [i for i in range(3000000, 10000001) if issimple(i)]
# print(A)
count = 0
sr = 0
for i in range(len(A)-1):
    if A[i] == A[i+1]-2:
        count += 1
        sr = (A[i] + A[i+1])/2

print(count, sr)