def first_letters(name):
    f_n, s_n = name.split()
    result = f_n[0] + '.' + s_n[0] + '.'
    return result.upper()


full_name = input('->')
print(first_letters(full_name))