VOWELS = 'aeiou'
def is_vow(inp):
    for i in range(len(inp)):
        if chr(inp[i]) in VOWELS:
            inp[i] = chr(inp[i])
    return inp


A = [100, 100, 116, 105, 117, 121]  # [100,100,116,105,117,121]

print(is_vow(A))