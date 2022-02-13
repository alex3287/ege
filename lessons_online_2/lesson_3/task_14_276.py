DIGITS = '0123456789№#@$*'


def ten_to_q(number, base):
    if number < base:
        return DIGITS[number]
    return ten_to_q(number//base, base) + DIGITS[number%base]


temp = 10000 + 625**25 + 5**100
print(ten_to_q(temp, 15))