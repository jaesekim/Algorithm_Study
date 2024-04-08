for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    maze[1][1], maze[13][13] = 1, 0
    answer = 0
    stack = [(1, 1)]
    while stack:
        x, y = stack.pop()
        if (x, y) == (13, 13):
            answer = 1
            break
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 16 and 0 <= ny < 16 and not maze[nx][ny]:
                maze[nx][ny] = 1
                stack.append((nx, ny))
    print(f"#{tc} {answer}")
