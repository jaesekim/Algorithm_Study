for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for x in range(N):
        for y in range(M):
            cur = arr[x][y]
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    cur += arr[nx][ny]
            answer = max(answer, cur)
    print(f"#{tc} {answer}")
