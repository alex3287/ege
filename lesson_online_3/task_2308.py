DIGITS = '0123456789abcdef'


def ten_to_q(number, base):
    if number < base:
        return DIGITS[number]
    return ten_to_q(number//base, base) + DIGITS[number%base]


for i in range(30, 0, -1):
    if ten_to_q(i, 5)[0] == '3':
        print(i, ten_to_q(i, 5))

print(ten_to_q(357, 7))