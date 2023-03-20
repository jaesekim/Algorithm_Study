from collections import deque


def validation(h, n):
    mx_value = 0
    for p in range(h):
        for q in range(n):
            if 0 in box[p][q][:]:
                return print(-1)
            if max(box[p][q][:]) >= mx_value:
                mx_value = max(box[p][q][:])
    return print(mx_value - 1)


M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
queue = deque()

for height in range(H):
    for i in range(N):
        for j in range(M):
            if box[height][i][j] == 1:
                queue.append((height, i, j))

# bfs
while queue:
    h, x, y = queue.popleft()
    for dh, dx, dy in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        nh = h + dh
        nx = x + dx
        ny = y + dy
        if 0 <= nh < H and 0 <= nx < N and 0 <= ny < M and not box[nh][nx][ny]:
            box[nh][nx][ny] = box[h][x][y] + 1
            queue.append((nh, nx, ny))
validation(H, N)