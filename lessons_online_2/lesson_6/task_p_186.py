s = open('input.txt').readline()
# print(s)

count = 0
i = 0
while i < len(s):
    if s[i] == '7':
        phone = s[i:i+11]
        if phone.isdigit():
            if len(phone) == 11 and int(phone[0])+int(phone[1]) == int(phone[-1])+int(phone[-2]):
                count += 1
    i += 1
print(count)