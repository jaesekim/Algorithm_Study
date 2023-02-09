c, r = map(int, input().split())
target = int(input())

dx = [0, 1, 0, -1] #상,우,하,좌
dy = [1, 0, -1, 0]
num = 0 #계속 더해갈 숫자
if c * r < target: #타깃 숫자가 공연장 크기보다 클 때
    print(0)
else:
    graph = [[0] * (r + 1) for _ in range(c + 1)]
    x = 1
    y = 0
    k = 0
    while target != num:
        #if num < c: #k는 dx, dy의 인덱스

        if (0 < x+dx[k] <= c) and (0 < y+dy[k] <= r) and (graph[x+dx[k]][y+dy[k]] == 0):
            x += dx[k]
            y += dy[k]
            graph[x][y] += 1
            num += 1
        else:
            k = (k + 1) % 4
    print(x, y)