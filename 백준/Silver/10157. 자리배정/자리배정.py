C, R = map(int, input().split())
queue= int(input())
if C * R < queue:
    print(0)
else:
    d_row = [0, 1, 0, -1]  # 행을 뺄셈해 줄 변수
    d_col = [1, 0, -1, 0]  # 열을 뺄셈해 줄 변수
    x = 1
    y = 0
    num = 0
    idx = 0
    route = [[0] * (R + 1) for _ in range(C + 1)]
    while num != queue:
        if (1 <= x + d_row[idx] <= C) and (1 <= y + d_col[idx]<= R) and (not route[x + d_row[idx]][y + d_col[idx]]):
            x += d_row[idx]
            y += d_col[idx]
            route[x][y] = 1
            num += 1
        else:
            idx = (idx + 1) % 4
    print(x, y)