# 3, 4, 5, 6, ...
D = '0123456789ABCDEFJIKLP'


def ten_to_q(number, base):
    if number < base:
        return D[number]
    return ten_to_q(number//base, base) + D[number % base]


for i in range(3, 21):
    print(i, ten_to_q(338, i))