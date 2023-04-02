from collections import deque

def bfs(nodes, others, nums):
    cnt = 0
    visited = [0] * (N + 1)
    for n in others:
        visited[n] = 1
    queue = deque()
    queue.append(nodes[0])  # 시작 위치
    visited[nodes[0]] = 1
    while queue:
        cur = queue.popleft()
        cnt += 1
        if cnt == nums:
            break
        for w in range(1, N+1):
            if w in graph[cur] and not visited[w]:
                visited[w] = 1
                queue.append(w)
    if 0 in visited[1:]:
        return 0
    return 1


def pop_sum(nodes):
    total = 0
    for node in nodes:
        total += populations[node]
    return total

N = int(input())
populations = list(map(int, input().split()))
populations.insert(0, 0)
graph = {}
for zone in range(1, N+1):
    graph[zone] = list(map(int, input().split()))[1:]

min_value = 1e9
flag = 0

# 부분 집합 두 개로 나누기
for i in range(1 << N):
    area1 = []
    area2 = []
    for j in range(N):
        if i & (1 << j):
            area1.append(j+1)
        else:
            area2.append(j+1)
    if 0 < len(area1) < N:
        if bfs(area1, area2, len(area1)) and bfs(area2, area1, len(area2)):
            flag = 1
            min_value = min(min_value, abs(pop_sum(area1) - pop_sum(area2)))
if not flag:
    print(-1)
else:
    print(min_value)
