di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]  # 상 하 좌 우
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    balloon = [list(map(int, input().split())) for _ in range(N)]
    mx_cnt = 0
    for x in range(N):
        for y in range(M):
            tmp_cnt = balloon[x][y]
            for idx in range(4):
                for mul in range(1, balloon[x][y]+1):
                    if 0 <= x + di[idx] * mul < N and 0 <= y + dj[idx] * mul < M:
                        tmp_cnt += balloon[x + di[idx] * mul][y + dj[idx] * mul]
            if tmp_cnt > mx_cnt:
                mx_cnt = tmp_cnt
    print(f"#{tc} {mx_cnt}")