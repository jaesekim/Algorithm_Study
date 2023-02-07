for no in range(1, 11):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    route_list = []
    for fin_idx, fin in enumerate(ladder[-1]):
        if fin == 2:
            break
    finish = (99, fin_idx)
    route_list.append(finish)  # 시작지점 append
    row = 99
    col = fin_idx
    while row >= 0:
        if (0 <= col - 1 < 100) and (ladder[row][col-1]) and ((row, col-1) not in route_list):  # 왼쪽 검사 & 이동
            col -= 1
            route_list.append((row, col))
        elif (0 <= col + 1 < 100) and (ladder[row][col+1]) and ((row, col+1) not in route_list):  # 오른쪽 검사 & 이동
            col += 1
            route_list.append((row, col))
        else:
            row -= 1
            route_list.append((row, col))
    print(f"#{no} {col}")