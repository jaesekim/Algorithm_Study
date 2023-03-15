from collections import deque


def bfs(n):
    cnt = 0
    queue = deque()
    for start in range(1, n+1):
        if nodes[start] and not visited[start]:
            queue.append(start)
            visited[start] = 1
            cnt += 1
            while queue:
                cur = queue.popleft()
                for w in range(1, n+1):
                    if nodes[cur][w] and not visited[w]:
                        queue.append(w)
                        visited[w] = 1
    return print(cnt)


N, M = map(int, input().split())
nodes = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    p, q = map(int, input().split())
    nodes[p][q] = 1
    nodes[q][p] = 1
bfs(N)
