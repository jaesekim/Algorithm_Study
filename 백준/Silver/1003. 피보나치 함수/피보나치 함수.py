def recurrence(n):
    arr = [[1, 0], [0, 1]]
    if not n or n == 1:
        return print(*arr[n])
    else:
        for i in range(2, n+1):
            arr.append([arr[i-2][0] + arr[i-1][0], arr[i-2][1] + arr[i-1][1]])
        return print(*arr[-1])


T = int(input())
for _ in range(T):
    recurrence(int(input()))
