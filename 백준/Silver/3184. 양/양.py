from collections import deque

R, C = map(int, input().split())
yard = [list(input()) for _ in range(R)]
total_sheep = 0
total_wolves = 0

queue = deque()
for i in range(R):
    for j in range(C):
        if yard[i][j] != '#':
            sheep = 0
            wolf = 0
            if yard[i][j] == 'v':
                wolf += 1
            elif yard[i][j] == 'o':
                sheep += 1
            yard[i][j] = '#'
            queue.append((i, j))
            while queue:
                x, y = queue.popleft()
                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ni = x + di
                    nj = y + dj
                    if 0 <= ni < R and 0 <= nj < C and yard[ni][nj] != '#':
                        if yard[ni][nj] == 'o':
                            sheep += 1
                        elif yard[ni][nj] == 'v':
                            wolf += 1
                        yard[ni][nj] = '#'
                        queue.append((ni, nj))
            if wolf < sheep:
                total_sheep += sheep
            else:
                total_wolves += wolf
print(total_sheep, total_wolves)