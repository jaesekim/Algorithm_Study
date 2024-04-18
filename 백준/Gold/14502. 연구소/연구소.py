import sys
from collections import deque
from itertools import combinations
import copy

input = sys.stdin.readline


def safe_area(arr):
    area = 0
    for row in arr:
        for col in row:
            if not col:
                area += 1
    return area


def bfs(arr, starts):
    queue = deque()
    for start in starts:
        queue.append(start)
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not arr[nx][ny]:
                arr[nx][ny] = 2
                queue.append((nx, ny))
    return safe_area(arr)


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
coordinate = []
promising = []
virus = []
answer = 0
for r in range(N):
    for c in range(M):
        coordinate.append((r, c))
        if lab[r][c] == 2:
            virus.append((r, c))

all_cases = list(map(list, combinations(coordinate, 3)))
for items in all_cases:
    cnt = 0
    for i, j in items:
        if not lab[i][j]:  # 바이러스가 옮길 수 있는 곳이라면
            cnt += 1
    if cnt == 3:
        for p, q in items:
            lab[p][q] = 1
        answer = max(answer, bfs(copy.deepcopy(lab), virus))
        for p, q in items:
            lab[p][q] = 0
print(answer)
