# abba

def check_string(string):
    if string == string[::-1]:
        return True
    return False


s = input()
print(check_string(s))