N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(N)]
cost = [[0] * M for _ in range(N)]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
queue = [(0, 0)]
cost[0][0] = 1
while queue:
    cur = queue.pop(0)
    if cur == (N-1, M-1):
        answer = cost[cur[0]][cur[1]]
    for idx in range(4):
        if 0 <= cur[0] + di[idx] < N and 0 <= cur[1] + dj[idx] < M \
                and maze[cur[0]+di[idx]][cur[1]+dj[idx]] and not cost[cur[0]+di[idx]][cur[1]+dj[idx]]:
            queue.append((cur[0]+di[idx], cur[1]+dj[idx]))
            cost[cur[0]+di[idx]][cur[1]+dj[idx]] = cost[cur[0]][cur[1]] + 1
print(answer)