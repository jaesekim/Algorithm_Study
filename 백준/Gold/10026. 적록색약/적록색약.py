from collections import deque


def bfs_c(visited, n):
    """
    :param visited: array of visited or not
    :param n: n x n matrix
    :return: numbers of zone
    """
    queue = deque()
    zone = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = 1
                zone += 1
                queue.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ni = x + di
                        nj = y + dj
                        if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] \
                                and arr[x][y] == arr[ni][nj]:
                            visited[ni][nj] = 1
                            queue.append((ni, nj))
    return zone


def bfs_cw(visited, n):
    queue = deque()
    zone = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = 1
                zone += 1
                queue.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ni = x + di
                        nj = y + dj
                        if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                            if arr[x][y] == 'B' and arr[ni][nj] == 'B':
                                visited[ni][nj] = 1
                                queue.append((ni, nj))
                            elif arr[x][y] == 'R' and (arr[ni][nj] == 'R' or arr[ni][nj] == 'G'):
                                visited[ni][nj] = 1
                                queue.append((ni, nj))
                            elif arr[x][y] == 'G' and (arr[ni][nj] == 'R' or arr[ni][nj] == 'G'):
                                visited[ni][nj] = 1
                                queue.append((ni, nj))
    return zone


N = int(input())
arr = [list(input()) for _ in range(N)]
color = [[0] * N for _ in range(N)]
color_weak = [[0] * N for _ in range(N)]
print(bfs_c(color, N), bfs_cw(color_weak, N))
