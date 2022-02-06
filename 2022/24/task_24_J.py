with open('24_J.txt') as fin:
    s = fin.readline()

tik = s.count('TIK')
tok = s.count('TOK')
print(tik+tok)