from collections import deque


def blank(p, q, s):
    if s == 0 or s == 2:
        if house[p][q]:
            return 0
    else:
        if house[p][q] or house[p-1][q] or house[p][q-1]:
            return 0
    return 1


N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
queue.append((0, 1, 0))  # i, j, 파이프 상태
# 파이프 상태 0: 가로, 1: 대각선, 2: 세로
cnt = 0
if house[-1][-1]:
    print(cnt)
else:
    while queue:
        i, j, status = queue.pop()
        if i == N - 1 and j == N - 1:
            cnt += 1
            continue
        if status == 0:    # 현재 파이프가 가로일 때
            for idx, delta in enumerate(((0, 1), (1, 1))):
                ni, nj = i + delta[0], j + delta[1]
                if 0 <= ni < N and 0 <= nj < N:
                    if blank(ni, nj, idx):
                        queue.append((ni, nj, idx))
        elif status == 1:  # 현재 파이프가 대각선일 때
            for idx, delta in enumerate(((0, 1), (1, 1), (1, 0))):
                ni, nj = i + delta[0], j + delta[1]
                if 0 <= ni < N and 0 <= nj < N:
                    if blank(ni, nj, idx):
                        queue.append((ni, nj, idx))
        else:              # 현재 파이프가 세로일 때
            for idx, delta in enumerate(((1, 1), (1, 0))):
                ni, nj = i + delta[0], j + delta[1]
                if 0 <= ni < N and 0 <= nj < N:
                    if blank(ni, nj, idx+1):
                        queue.append((ni, nj, idx+1))
    print(cnt)