cnt = int(input())

for test_no in range(1, cnt + 1):
    by = int(input())
    array = [list(map(int, input().split())) for _ in range(by)]
    print(f"#{test_no}")
    for p in range(by):
        dummy_1 = []
        for q in range(by-1, -1, -1):
            dummy_1.append(array[q][p])
        dummy_2 = []
        for r in range(by-1, -1, -1):
            dummy_2.append(array[by - p - 1][r])
        dummy_3 = []
        for s in range(by):
            dummy_3.append(array[s][by - p - 1])
        print(f'{"".join(list(map(str, dummy_1)))} {"".join(list(map(str, dummy_2)))} {"".join(list(map(str, dummy_3)))}')