import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
ladder = {}
snake = {}
board = list(range(1, 101))
visited = [0] * 101
for _ in range(N):
    start, end = map(int, input().split())
    ladder[start] = end
for _ in range(M):
    start, end = map(int, input().split())
    snake[start] = end
queue = deque()
queue.append(1)
while queue:
    cur = queue.popleft()
    if cur == 100:
        print(visited[-1])
        break
    for dx in range(1, 7):
        nx = cur + dx
        if ladder.get(nx, 0):
            nx = ladder[nx]
        elif snake.get(nx, 0):
            nx = snake[nx]
        if 1 <= nx <= 100 and not visited[nx]:
            visited[nx] = visited[cur] + 1
            queue.append(nx)
