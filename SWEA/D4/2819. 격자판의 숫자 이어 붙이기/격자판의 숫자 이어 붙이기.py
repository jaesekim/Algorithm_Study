def dfs(x, y, cnt, chars):
    global answer
    if cnt == 7:
        answer.add(chars)
        return
    chars += arr[x][y]
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, cnt+1, chars)


T = int(input())
for tc in range(1, T+1):
    arr = [input().split() for _ in range(4)]
    answer = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, 0, '')
    print(f"#{tc} {len(answer)}")
