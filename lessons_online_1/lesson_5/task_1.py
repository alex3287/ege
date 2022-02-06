# 310
# из любой СС в 10-ю

n = int('33', 4)

# из 10-й в любую другую

DIGITS = '0123456789ABCDEF'


def ten_to_q(number, base):
    if number < base:
        return DIGITS[number]
    return ten_to_q(number // base, base) + DIGITS[number % base]


for x in range(4, 17):
    if int('21', x) * int('13', x) == int('313', x):
        print(x)

