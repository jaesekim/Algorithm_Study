T = int(input())
for test_no in range(1, T+1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    min_cnt = 1e9

    for white in range(N-2):
        for blue in range(white+1, N-1):
            cnt = 0
            for x in flag[:white+1]:
                for idx in range(M):
                    if x[idx] != 'W':
                        cnt += 1
            for y in flag[white+1:blue+1]:
                for idx in range(M):
                    if y[idx] != 'B':
                        cnt += 1
            for z in flag[blue+1:]:
                for idx in range(M):
                    if z[idx] != 'R':
                        cnt += 1
            if cnt < min_cnt:
                min_cnt = cnt
    print(f"#{test_no} {min_cnt}")