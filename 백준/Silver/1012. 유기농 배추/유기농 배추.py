from collections import deque

for tc in range(int(input())):
    M, N, K = map(int, input().split())
    field = [[0] * N for _ in range(M)]
    visited = [[0] * N for _ in range(M)]
    queue = deque()
    answer = 0
    for _ in range(K):
        a, b = map(int, input().split())
        field[a][b] = 1
    for i in range(M):
        for j in range(N):
            if field[i][j] and not visited[i][j]:
                answer += 1
                queue.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < M and 0 <= ny < N and field[nx][ny] and not visited[nx][ny]:
                            visited[nx][ny] = 1
                            queue.append((nx, ny))
    print(answer)
