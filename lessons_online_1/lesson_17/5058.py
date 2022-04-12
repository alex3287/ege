D = '0123456789ABCDEF'


def ten_to_q(number, base):
    if number < base:
        return D[number]
    return ten_to_q(number // base, base) + D[number % base]


for i in range(2, 17):
    print(i, '->', ten_to_q(66, i), ten_to_q(40, i))