def array2(string):
    result = ''
    for i in string:
        if i == ',':
            result += ' '
        else:
            result += i
    return result


def array2(string):
    if len(string) < 5:
        return None
    string = string.replace(',', ' ')
    i1 = string.find(' ')
    i2 = string.rfind(' ')
    string = string[i1+1:i2]
    return string


def array(string):
    if string:
        A = string.split(',')
        if len(A) < 3:
            return None
        s = ' '.join(A[1:-1])
        return s
    return None


s = 'fbe,a52,24,1a,2f,52c'  # 'a52 24 1a 2f'
print(array(s))