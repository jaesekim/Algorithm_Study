import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
flag = False

while arr != [1, 2, 3, 4, 5]:
    if arr[0] > arr[1]:
        arr[0], arr[1] = arr[1], arr[0]
        for num in arr:
            print(num, end=" ")
    if arr[1] > arr[2]:
        arr[1], arr[2] = arr[2], arr[1]
        for num in arr:
            print(num, end=" ")
    if arr[2] > arr[3]:
        arr[2], arr[3] = arr[3], arr[2]
        for num in arr:
            print(num, end=" ")
    if arr[3] > arr[4]:
        arr[3], arr[4] = arr[4], arr[3]
        for num in arr:
            print(num, end=" ")
    else:
        continue
    print()









