di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# 우, 하, 좌, 상

for _ in range(1, 11):
    no = int(input())
    maze = [list(map(int, list(input()))) for _ in range(16)]

    for x in range(16):
        for y in range(16):
            if maze[x][y] == 2:
                dx, dy = x, y  # 시작 좌표
                maze[x][y] = 0
            elif maze[x][y] == 3:
                ax, ay = x, y  # 도착 좌표
                maze[x][y] = 0

    # maze 출발, 도착지점도 0으로 초기화
    stack = []  # 스택을 위한 리스트
    answer = 0  # 답을 담아줄 변수
    stack.append([dx, dy])
    while stack:
        cur = stack.pop()
        if cur == [ax, ay]:
            answer = 1
            break
        if not maze[cur[0]][cur[1]]:
            maze[cur[0]][cur[1]] = 1
            for i in range(4):
                if 0 <= cur[0] + di[i] < 16 and 0 <= cur[1] + dj[i] < 16 and not maze[cur[0] + di[i]][cur[1] + dj[i]]:
                    stack.append([cur[0] + di[i], cur[1] + dj[i]])
    print(f"#{no} {answer}")