N = int(input())
arr = [0, 0, 1, 1]
if N <= 3:
    print(arr[N])
else:
    for i in range(4, N+1):
        if not i % 2 and not i % 3:
            arr.append(min(arr[i // 2] + 1, arr[i // 3] + 1, arr[i - 1] + 1))
        elif not i % 2:
            arr.append(min(arr[i // 2] + 1, arr[i-1] + 1))
        elif not i % 3:
            arr.append(min(arr[i // 3] + 1, arr[i-1] + 1))
        else:
            arr.append(arr[i - 1] + 1)
    print(arr[-1])