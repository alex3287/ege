DIGITS = '0123456789abcdef'


def ten_to_q(number, base):
    if number < base:
        return DIGITS[number]
    return ten_to_q(number//base, base) + DIGITS[number%base]


for i in range(10, 18):
    print(ten_to_q(i, 5))
