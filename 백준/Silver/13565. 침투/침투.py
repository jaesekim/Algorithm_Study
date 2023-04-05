from collections import deque


# def bfs(i, j):
#     queue = deque()
#     queue.append((i, j))


M, N = map(int, input().split())  # M: row, N: col
arr = [list(map(int, list(input()))) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
flag = 0
answer = 0
for start in range(N):
    if flag:
        break
    if not arr[0][start]:
        queue = deque()
        queue.append((0, start))
        visited[0][start] = 1
        while queue:
            x, y = queue.popleft()
            if x == M - 1:  # 끝까지 갔다면
                answer = 1
                flag = 1
                break
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < M and 0 <= ny < N and not arr[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
        visited = [[0] * N for _ in range(M)]
if answer:
    print("YES")
else:
    print("NO")