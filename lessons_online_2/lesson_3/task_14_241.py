DIGITS = '0123456789abcdef'


def ten_to_q(number, base):
    if number < base:
        return DIGITS[number]
    return ten_to_q(number//base, base) + DIGITS[number%base]


for i in range(81, 729):
    x = ten_to_q(i, 9)
    if x.count('3') > 0:
        temp = i * 3
        temp = ten_to_q(temp, 9)
        if len(temp) == 3:
            print(i)

print()
print(ten_to_q(237+84, 9))


