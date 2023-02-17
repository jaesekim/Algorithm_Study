# 상, 하, 좌, 우, 왼쪽위, 오른쪽위, 왼쪽아래, 오른쪽아래
di = [-1, 1, 0, 0, -1, -1, 1, 1]
dj = [0, 0, -1, 1, -1, 1, -1, 1]

T = int(input())
for no in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    landing_point = 0  # 총 착륙 지점 개수
    for i in range(N):
        for j in range(M):
            cnt = 0  # 각 지점 착륙 가능 여부 판단
            for delta in range(8):
                if 0 <= i + di[delta] < N and 0 <= j + dj[delta] < M:
                    if arr[i][j] > arr[i + di[delta]][j + dj[delta]]:
                        cnt += 1
                else:
                    continue
            if cnt >= 4:
                landing_point += 1
    print(f"#{no} {landing_point}")