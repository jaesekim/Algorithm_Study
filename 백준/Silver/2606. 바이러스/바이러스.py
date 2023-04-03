from collections import deque

nums = int(input())
network = {}
for i in range(1, nums+1):
    network[i] = []
edges = int(input())
answer = 0
visited = [0] * (nums + 1)
for _ in range(edges):
    n1, n2 = map(int, input().split())
    network[n1].append(n2)
    network[n2].append(n1)
queue = deque()
queue.append(1)
visited[1] = 1
while queue:
    cur = queue.popleft()
    for w in network[cur]:
        if not visited[w]:
            visited[w] = 1
            answer += 1
            queue.append(w)
print(answer)