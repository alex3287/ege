number_1 = 10
number_2 = 10

if number_1 > number_2:
    number_2 += 8
else:
    number_1 += 5

if number_1 % 2 == 0:
    number_2 += 8
elif number_1 % 3 == 0:
    number_2 += 5
elif number_2 > 0:
    number_2 += 10
else:
    number_1 = 9

print(number_2)

