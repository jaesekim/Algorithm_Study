n = int(input())
arr = [0, 1]    
if n <= 1:
    print(n)
else:
    start = 2
    while start <= n:
        arr.append(arr[start - 1] + arr[start - 2])
        start += 1
    print(arr[-1])