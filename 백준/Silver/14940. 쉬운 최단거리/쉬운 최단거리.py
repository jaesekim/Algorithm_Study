from collections import deque


def bfs(si, sj, N, M):
    queue = deque()
    queue.append((si, sj))
    while queue:
        cur = queue.popleft()
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni = cur[0] + di
            nj = cur[1] + dj
            if 0 <= ni < N and 0 <= nj < M and not cost[ni][nj] and arr[ni][nj]:
                cost[ni][nj] = cost[cur[0]][cur[1]] + 1
                queue.append((ni, nj))


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cost = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            start = (i, j)
            break
bfs(start[0], start[1], n, m)

for x in range(n):
    for y in range(m):
        if not cost[x][y] and arr[x][y] == 1:
            cost[x][y] = -1
cost[start[0]][start[1]] = 0

for lst in cost:
    print(*lst)
