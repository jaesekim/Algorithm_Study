import sys
import collections

input = sys.stdin.readline


def mature_days(m, n):
    minimum = -1
    for x in range(n):
        for y in range(m):
            if not arr[x][y]:
                return -1
            minimum = max(minimum, arr[x][y] - 1)  # 처음 토마토 익은것 1 더해져있던거 빼주기
    return minimum


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
queue = collections.deque()
answer = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append((i, j))  # 시작점 찾기

while queue:
    cur = queue.popleft()
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = cur[0] + di, cur[1] + dj
        if 0 <= nx < N and 0 <= ny < M and not arr[nx][ny]:
            queue.append((nx, ny))
            arr[nx][ny] = arr[cur[0]][cur[1]] + 1
print(mature_days(M, N))
