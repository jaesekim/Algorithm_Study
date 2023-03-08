from collections import deque


def val_answer():
    mx_value = 0
    for lst in tomato:
        if 0 in lst:
            return print(-1)
        if max(lst) > mx_value:
            mx_value = max(lst)
    return print(mx_value - 1)


M, N = map(int, input().split())  # N: 행, M: 열
tomato = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i, j))
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
# bfs
while queue:
    cur = queue.popleft()
    for idx in range(4):
        ni = cur[0] + di[idx]
        nj = cur[1] + dj[idx]
        if 0 <= ni < N and 0 <= nj < M and not tomato[ni][nj]:
            queue.append((ni, nj))
            tomato[ni][nj] = tomato[cur[0]][cur[1]] + 1
val_answer()
