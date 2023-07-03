from collections import deque

T = int(input())  # numbers of test cases
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
for tc in range(T):
    L = int(input())  # length of chess board of one side
    start_x, start_y = map(int, input().split())  # coordinate of start point
    end_x, end_y = map(int, input().split())       # coordinate of end point
    board = [[0] * L for _ in range(L)]
    queue = deque()
    queue.append((start_x, start_y))
    board[start_x][start_y] = 0
    while queue:
        x, y = queue.popleft()
        if x == end_x and y == end_y:
            print(board[x][y])
            break
        for idx in range(8):
            nx, ny = x + dx[idx], y + dy[idx]
            if 0 <= nx < L and 0 <= ny < L and not board[nx][ny]:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))
