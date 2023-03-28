N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N):
    for j in range(3):
        if j == 0:
            cost[i][j] += min(cost[i-1][1], cost[i-1][2])
        elif j == 1:
            cost[i][j] += min(cost[i-1][0], cost[i-1][2])
        elif j == 2:
            cost[i][j] += min(cost[i-1][0], cost[i-1][1])
print(min(cost[-1]))