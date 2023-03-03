def validation(test, by):
    dx = [-1, -1, 1, 1]  # 좌상 우상 좌하 우하
    dy = [-1, 1, -1, 1]

    for row in go:
        for i in range(by - 4):
            if row[i:i+5].count('o') == 5:
                return print(f"#{test} YES")
    for col in go_t:
        for i in range(by - 4):
            if col[i:i+5].count('o') == 5:
                return print(f"#{test} YES")
    for i in range(by):
        for j in range(by):
            p = i
            q = j
            if go[i][j] == 'o':
                for idx in range(4):    # 델타 대각선 네 방향 탐색
                    cnt = 1
                    for _ in range(by):  # 오목 되는지 확인
                        if 0 <= p + dx[idx] < by and 0 <= q + dy[idx] < by and go[p+dx[idx]][q+dy[idx]] == 'o':
                            cnt += 1
                            p += dx[idx]
                            q += dy[idx]
                        if cnt >= 5:
                            return print(f"#{test} YES")
    return print(f"#{test} NO")


T = int(input())
for test_no in range(1, T+1):
    N = int(input())
    go = [list(input()) for _ in range(N)]
    go_t = list(map(list, zip(*go)))
    validation(test_no, N)