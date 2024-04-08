import sys

input = sys.stdin.readline


def dfs(x, y, m, n):
    stack = [(x, y)]
    while stack:
        cur = stack.pop()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = cur[0] + dx, cur[1] + dy
            if 0 <= nx < m and 0 <= ny < n and field[nx][ny]:
                field[nx][ny] = 0
                stack.append((nx, ny))


for _ in range(int(input())):
    M, N, K = map(int, input().split())
    field = [[0] * N for _ in range(M)]
    for _ in range(K):
        i, j = map(int, input().split())
        field[i][j] = 1
    answer = 0
    for x in range(M):
        for y in range(N):
            if field[x][y]:
                answer += 1
                field[x][y] = 0
                dfs(x, y, M, N)
    print(answer)
