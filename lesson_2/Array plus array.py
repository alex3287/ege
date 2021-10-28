def array_plus_array(arr1, arr2):
    sum_A = 0
    sum_B = 0
    for i in arr1:
        sum_A += i
    for j in arr2:
        sum_B += j
    return sum_A + sum_B


A = [1, 2, 3]
B = [4, 5, 6]
# 21

print(array_plus_array(A, B))