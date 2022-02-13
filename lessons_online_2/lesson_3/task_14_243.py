DIGITS = '0123456789abcdef'


def ten_to_q(number, base):
    if number < base:
        return DIGITS[number]
    return ten_to_q(number//base, base) + DIGITS[number%base]


a = int('25', 8)
b = int('24', 16)
c = int('43', 8) - int('1B', 16)
d = int('110101', 2) + int('13', 8)
x = 16**a + 4**b - 8**c -2**d + 31
x = hex(x)[2:]
A = [int(i) if i.isdigit() else int(i, 16) for i in list(x)]
print(x) #19
min_num = min(A)
max_num = max(A)
print(A, DIGITS[min_num], DIGITS[max_num])
s = '123'
# print(s.isdigit())
