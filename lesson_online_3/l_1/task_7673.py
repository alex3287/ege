DIGITS = '0123456789abcdef'


def ten_to_q(number, base):
    if number < base:
        return DIGITS[number]
    return ten_to_q(number//base, base) + DIGITS[number%base]


for x in range(3, 17):
    if int('121', x) + 1 == int('101', 7):
        print(x)
        break

print(ten_to_q(x, 3))
