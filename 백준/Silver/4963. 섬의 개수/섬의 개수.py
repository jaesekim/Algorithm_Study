while True:
    w, h = map(int, input().split())  # w: 열, h: 행
    if not w or not h:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    # 1: 땅, 0: 바다
    di = [1, -1, 0, 0, -1, -1, 1, 1]
    dj = [0, 0, 1, -1, -1, 1, -1, 1]
    island = 0
    stack = []
    for i in range(h):
        for j in range(w):
            if arr[i][j] and not visited[i][j]:
                island += 1
                visited[i][j] = 1
                stack.append((i, j))
            while stack:
                cur = stack.pop()
                for idx in range(8):
                    if 0 <= cur[0] + di[idx] < h and 0 <= cur[1] + dj[idx] < w \
                            and not visited[cur[0]+di[idx]][cur[1]+dj[idx]] and arr[cur[0]+di[idx]][cur[1]+dj[idx]]:
                        visited[cur[0]+di[idx]][cur[1]+dj[idx]] = 1
                        stack.append((cur[0]+di[idx], cur[1]+dj[idx]))
    print(island)
