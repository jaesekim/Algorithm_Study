from collections import deque

N = int(input())
graph = {}
for key in range(N+1):
    graph[key] = []
visited = [0] * (N + 1)
parent = [0] * (N + 1)
for _ in range(N-1):
    ni, nj = map(int, input().split())
    graph[ni].append(nj)
    graph[nj].append(ni)
queue = deque()
queue.append(1)
visited[1] = 1  # 루트노드는 항상 1
while queue:
    cur_key = queue.popleft()  # 딕셔너리의 키 값 popleft
    cur_lst = graph[cur_key]
    for w in cur_lst:
        if not visited[w]:  # 현재 노드와 연결된 노드가 있고 방문하지 않았다면
            parent[w] = cur_key
            queue.append(w)
            visited[w] = 1
for par in parent[2:]:
    print(par)