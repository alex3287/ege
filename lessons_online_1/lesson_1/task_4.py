s = 'Hello world! 908797'
# s = 'Hetlo world! 908797'
print(len(s))
print(s[-1])
# s[2] = 't'
print(s[1:4])
print(s[:4])
print(s[12:-1])
s = s[:2] + 't' + s[3:]
print(s)
print(s[::-1])