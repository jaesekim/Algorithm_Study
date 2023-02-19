di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]  # 우 하 좌 상
T = int(input())
for no in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    i = 0
    j = -1
    idx = 0  # 델타탐색 인덱스
    nbr = 1  # 값을 넣어줄 변수
    while nbr <= N * N:
        if 0 <= i + di[idx] < N and 0 <= j + dj[idx] < N and not arr[i + di[idx]][j + dj[idx]]:
            arr[i + di[idx]][j + dj[idx]] = nbr
            i += di[idx]
            j += dj[idx]
            nbr += 1
        else:
            idx = ((idx + 1) % 4)
    print(f"#{no}")
    for chars in arr:
        print(*chars)