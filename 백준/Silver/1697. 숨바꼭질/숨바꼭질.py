from collections import deque

N, K = map(int, input().split())
visited = [0] * 100001
queue = deque()
queue.append(N)
visited[N] = 1  # 방문 처리
while queue:
    cur = queue.popleft()
    if cur == K:
        print(visited[K] - 1)  # 초기에 임의로 더해줬던 값 빼 주기
        break
    for nx in [cur + 1, cur - 1, 2 * cur]:
        if 0 <= nx <= 100000 and not visited[nx]:
            visited[nx] = visited[cur] + 1
            queue.append(nx)
