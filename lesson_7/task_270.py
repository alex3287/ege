# алгоритм суммы цифр числа
def sum_digit(n):
    # вариант 1
    # return sum(map(int, str(n)))
    # вариант 2
    # s = 0
    # for i in str(n):
    #     s += int(i)
    # return s
    # вариант 3
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


A = [int(i) for i in open('17-270.txt')]
# print(A)

count = 0
min_sum = 20001
sum_35 = 0

for i in A:
    if i % 35 == 0:
        sum_35 += sum_digit(i)

print(sum_35)
for i in range(len(A)-1):
    if (A[i] > sum_35 and A[i+1] <= sum_35 and hex(A[i+1])[-2:] == 'ef') or (A[i+1] > sum_35 and A[i] <= sum_35 and A[i] % 256 == 239):
        count += 1
        if A[i] + A[i+1] < min_sum:
            min_sum = A[i] + A[i+1]

print(count, min_sum)