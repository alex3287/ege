def devisions(number):
    k = 2
    arr = []
    while k*k <= number:
        if number % k == 0:
            arr.append(k)
            arr.append(number // k)
        k += 1
    return sorted(arr)


for i in range(174457, 174506):
    arr = devisions(i)
    if len(arr) == 2:
        print(arr, arr[0]*arr[1])