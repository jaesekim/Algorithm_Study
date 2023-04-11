from collections import deque

N = int(input())
apt = [list(map(int, list(input()))) for _ in range(N)]
complexes = []
for i in range(N):
    for j in range(N):
        if apt[i][j]:
            queue = deque()
            queue.append((i, j))
            cnt = 1
            apt[i][j] = 0
            while queue:
                x, y = queue.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and apt[nx][ny]:
                        apt[nx][ny] = 0
                        cnt += 1
                        queue.append((nx, ny))
            complexes.append(cnt)
complexes = sorted(complexes)
print(len(complexes))
for cpx in complexes:
    print(cpx)
