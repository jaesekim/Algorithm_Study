from collections import deque


def find_max(n, m):
    mx_value = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] != 'W' and visited[i][j] >= mx_value:
                mx_value = visited[i][j]
    return mx_value


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
queue = deque()
answer = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            queue.append((i, j))
            visited[i][j] = 1
            while queue:
                x, y = queue.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 'L' and not visited[nx][ny]:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))
        answer.append(find_max(N, M))
        visited = [[0] * M for _ in range(N)]
print(max(answer) - 1)
