def dev(number):
    A = []
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            A.append(i)
            if i != number // i:
                A.append(number // i)
            if len(A) > 2:
                break
    return A


# print(dev(25))
for i in range(174457, 174506):
# for i in range(2, 21):
    M = dev(i)
    if len(M) == 2:
        print(M)