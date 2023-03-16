def recurrence(n):
    # 점화식 초기값 설정. 인덱스 1부터 시작
    arr = [0, 1, 2]
    if n == 1 or n == 2:
        return print(arr[n] % 10007)
    else:
        for i in range(3, n+1):
            arr.append(arr[i-2] + arr[i-1])
        return print(arr[-1] % 10007)


recurrence(int(input()))
