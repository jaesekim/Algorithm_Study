from collections import deque

N = int(input())
graph = {}
for key in range(N + 1):
    graph[key] = []
visited = [0] * (N + 1)
for _ in range(N-1):
    ni, nj = map(int, input().split())
    graph[ni].append(nj)
    graph[nj].append(ni)
routes = 0
queue = deque()
queue.append(1)
visited[1] = 1
while queue:
    cur_key = queue.popleft()
    cur_lst = graph[cur_key]
    leaf_val = 0
    for w in cur_lst:
        if not visited[w] and graph[w]:
            visited[w] = visited[cur_key] + 1
            queue.append(w)
        else:
            leaf_val += 1
    if leaf_val == len(cur_lst):
        routes += (visited[cur_key] - 1)
if routes % 2:
    print("Yes")
else:
    print("No")
