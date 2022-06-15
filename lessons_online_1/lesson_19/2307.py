D = '01234'


def five(number):
    if number < 5:
        return D[number]
    return five(number//5) + D[number % 5]


for i in range(10, 18):
    print(five(i))