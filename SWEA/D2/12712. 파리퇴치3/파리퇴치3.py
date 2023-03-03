def mx_area(x, y, N, M):
    d1_x = [-1, 1, 0, 0]   # 상하좌우
    d1_y = [0, 0, -1, 1]   # + 모양
    d2_x = [-1, -1, 1, 1]  # 좌상 우상 좌하 우하
    d2_y = [-1, 1, -1, 1]  # x 모양
    d1_cnt = 0
    d2_cnt = 0
    cor = arr[x][y]
    for idx in range(4):
        p = x
        q = y
        for _ in range(M-1):
            p += d1_x[idx]
            q += d1_y[idx]
            if 0 <= p < N and 0 <= q < N:
                d1_cnt += arr[p][q]
    for idx in range(4):
        p = x
        q = y
        for _ in range(M-1):
            p += d2_x[idx]
            q += d2_y[idx]
            if 0 <= p < N and 0 <= q < N:
                d2_cnt += arr[p][q]
    return max(cor + d1_cnt, cor + d2_cnt)


T = int(input())
for test_no in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx_value = 0
    for i in range(N):
        for j in range(N):
            if mx_value <= mx_area(i, j, N, M):
                mx_value = mx_area(i, j, N, M)
    print(f"#{test_no} {mx_value}")