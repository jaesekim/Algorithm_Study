from collections import deque


N = int(input())
floors = [list(map(int, input().split())) for _ in range(N)]
# 최대 영역 개수
mx_areas = 1

# 가장 높은 지대 찾기
highest = 0
for floor in floors:
    highest = max(highest, max(floor))
cur = 1
while cur <= highest:
    visited = [[0] * N for _ in range(N)]
    areas = 0
    for i in range(N):
        for j in range(N):
            if floors[i][j] > cur and not visited[i][j]:
                areas += 1
                visited[i][j] = 1
                stack = deque()
                stack.append((i, j))
                while stack:
                    x, y = stack.pop()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and floors[nx][ny] > cur:
                            visited[nx][ny] = 1
                            stack.append((nx, ny))
    mx_areas = max(mx_areas, areas)
    cur += 1
print(mx_areas)
