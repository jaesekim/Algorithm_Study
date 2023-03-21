def bags(n):
    arr = [-1, -1, -1, 1, -1, 1]
    # N과 인덱스를 맞춰주기 위해 다 채워준다
    if 3 <= n <= 5:
        return print(arr[n])
    else:
        idx = 6
        while idx <= n:
            if not idx % 5:
                arr.append(idx // 5)
            elif arr[idx - 3] != -1:
                arr.append(arr[idx - 3] + 1)
            elif arr[idx - 3] == -1:
                arr.append(-1)
            idx += 1
        return print(arr[-1])


bags(int(input()))