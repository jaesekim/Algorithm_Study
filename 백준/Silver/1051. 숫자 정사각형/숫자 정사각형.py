def is_same(i, j, side):
    for x in [square[i][j + side], square[i + side][j], square[i + side][j + side]]:
        if square[i][j] != x:
            return 0
    return 1


N, M = map(int, input().split())
square = [list(map(int, list(input()))) for _ in range(N)]
square_t = list(map(list, zip(*square)))
side = min(N, M) - 1  # 한 변의 길이 최대값 - 1(인덱스 맞추기)
area = []
for i in range(N):
    for j in range(M):
        for idx in range(side, -1, -1):
            if 0 <= i + idx < N and 0 <= j + idx < M:
                if is_same(i, j, idx):
                    area.append((idx+1) ** 2)
print(max(area))