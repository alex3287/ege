def alg(N):
    two = bin(N)[2:]
    two += '01' if N % 2 == 0 else '10'
    R = int(two, 2)
    return R


for N in range(100):
    R = alg(N)
    if R > 102:
        print(N, '->', R)
        break