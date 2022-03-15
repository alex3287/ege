DIGITS = '0123456789abcdef'


def ten_to_q(number, base):
    if number < base:
        return DIGITS[number]
    return ten_to_q(number//base, base) + DIGITS[number%base]


for i in range(1, 100):
    if i % 5 == 0 and i % 3 == 0:
        print(i)