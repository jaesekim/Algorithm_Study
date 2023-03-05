N, M = map(int, input().split())
# 가로 0 세로 1
coordinates = {
    0: [0, M],
    1: [0, N]
}
area = []
for _ in range(int(input())):
    num, coord = map(int, input().split())
    coordinates[num].insert(-1, coord)
for key in coordinates:
    coordinates[key].sort()
for i in range(1, len(coordinates[1])):
    x = coordinates[1][i] - coordinates[1][i-1]
    for j in range(1, len(coordinates[0])):
        y = coordinates[0][j] - coordinates[0][j-1]
        area.append(x * y)
print(max(area))
