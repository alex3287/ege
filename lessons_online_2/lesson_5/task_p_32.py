#
#
def all_dev(number):
    A = [1, number]
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            A.append(i)
            if number//i != i:
                A.append(number//i)
    return A


count_max = 0
Dev = []
for i in range(394441, 394506):
    D = all_dev(i)
    if len(D) > count_max:
        count_max = len(D)
        Dev = D

print(count_max, Dev)