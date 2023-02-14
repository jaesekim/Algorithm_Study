T = int(input())
for t in range(1, T+1):
    arr = []
    n = int(input())
    for _ in range(n):
        arr.append([1])
    print(f'#{t}')

    for i in range(n):
        if i == 1:  # 두 번째 줄
            arr[i].append(1)
            continue
        if i > 1:  # 세 번째 줄 부터 계산 시작
            for j in range(i-1):
                tmp1 = arr[i-1][j] + arr[i-1][j+1]  # 더해주기
                arr[i].append(tmp1)
            arr[i].append(1)  # 마지막에 1 넣어주기

    for k in range(n):
        print(*arr[k])