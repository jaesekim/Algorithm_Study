from collections import deque

N, K = map(int, input().split())
virus = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
visited = [[0] * N for _ in range(N)]  # 방문 이력

while S:
    # 임시
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] ==  1:
                cnt += 1
    if cnt == N*N:
        break

    queue = deque()
    for num in range(1, K+1):  # num 은 현재 virus
        for i in range(N):
            for j in range(N):
                if virus[i][j] == num and not visited[i][j]:
                    queue.append((i, j, num))
                    visited[i][j] = 1
    while queue:
        x, y, v = queue.popleft()
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not virus[nx][ny]:
                virus[nx][ny] = v
    S -= 1
print(virus[X - 1][Y - 1])
