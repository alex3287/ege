# P=[2,10] и Q=[6,14] . Какова НАИБОЛЬШАЯ возможна длина интервала A


def f(x, A):
    return ((x in A) <= (x in P)) or (x in Q)


p1, p2, q1, q2 = 2, 10, 6, 14
P = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
Q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]


def f(x, A):
    return ((x in A) <= (x in P)) or (x in Q)


A = set([i / 10 for i in range(10, 201)])
for x in [i / 10 for i in range(10, 201)]:
    if not f(x, A):
        A.remove(x)

print(sorted(A))  # [2.0;14.0]    Длина = 14-2


# НАИМЕНЬШАЯ длина

def alg(A, x):
    return ((x in P) and (x in Q)) <= ((x in Q) and (x in A))


p1, p2, q1, q2 = 10, 39, 23, 58

P = [i / 10 for i in range(100, 391)]
Q = [i / 10 for i in range(230, 581)]

A = set()

for x in [i / 10 for i in range(50, 601)]:
    if not alg(A, x):
        A.add(x)
print(sorted(A))