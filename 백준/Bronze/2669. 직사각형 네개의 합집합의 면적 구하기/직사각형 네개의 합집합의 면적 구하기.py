area = set()
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for height in range(y1, y2):
        for width in range(x1, x2):
            area.add((width, height))
print(len(area))