count = 0
maxi = 0

for i in range(3201, 12876+1):
    if i%4==0 and i%7!=0 and i%11!=0 and i%13!=0 and i%19!=0:
        count += 1
        # if i > maxi:
        maxi = i

print(count, maxi)