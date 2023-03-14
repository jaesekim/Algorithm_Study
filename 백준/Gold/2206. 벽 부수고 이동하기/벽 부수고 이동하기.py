from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
# 삼차원 리스트 visited[row][col][0]: 벽 부수기 전 / visited[row][col][1]: 벽 부수기 후

queue = deque()
queue.append((0, 0, 0))
visited[0][0][0] = 1
answer = -1  # 도달하지 못하면 -1 출력
while queue:
    x, y, z = queue.popleft()
    # 종료조건: x, y 좌표가 목적 좌표일 때
    if x == N-1 and y == M-1:
        answer = visited[x][y][z]
        break
    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ni = x + di
        nj = y + dj
        if 0 <= ni < N and 0 <= nj < M:
            # 벽이 아닌 경우
            if not visited[ni][nj][z] and not maze[ni][nj]:
                # 뚫을 필요 없으므로 z = 0 현상 유지
                visited[ni][nj][z] = visited[x][y][z] + 1
                queue.append((ni, nj, z))
            # 다음 구간이 벽인데 아직 안뚫었었고 방문하지 않았다면
            # 한번 뚫으면 z는 1로 고정되어서 두 번 다시 뚫지 못 함.
            elif maze[ni][nj] and not z and not visited[ni][nj][1]:
                queue.append((ni, nj, 1))
                visited[ni][nj][1] = visited[x][y][0] + 1
                queue.append((ni, nj, 1))
print(answer)
