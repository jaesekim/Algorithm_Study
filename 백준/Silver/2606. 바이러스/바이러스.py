import sys
input = sys.stdin.readline

N = int(input())
network = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N + 1)
cnt = 0
stack = []

for _ in range(int(input())):
    n1, n2 = map(int, input().split())
    network[n1][n2] = 1
    network[n2][n1] = 1
stack.append(1)
visited[1] = 1

while stack:
    cur = stack.pop()
    for node in range(1, N+1):
        connected = network[cur][node]
        if not visited[node] and connected:
            cnt += 1
            visited[node] = 1
            stack.append(node)
print(cnt)
