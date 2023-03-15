from collections import deque

arr = [input().split() for _ in range(5)]
chars = set()
for i in range(5):
    for j in range(5):
        queue = deque()
        char = ''
        char += arr[i][j]
        queue.append((i, j, char))
        while queue:
            x, y, z = queue.popleft()
            if len(z) == 6:
                chars.add(z)
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ni = x + di
                nj = y + dj
                if 0 <= ni < 5 and 0 <= nj < 5 and len(z) < 6:
                    queue.append((ni, nj, z + arr[ni][nj]))
print(len(chars))