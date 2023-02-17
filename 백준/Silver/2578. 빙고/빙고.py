def check_bingo(arr):
    bingo_cnt = 0
    arr_t = list(map(list, zip(*arr)))  # arr 전치행렬
    # 가로 빙고 구하기
    for row in arr:
        if not sum(row):
            bingo_cnt += 1
    # 세로 빙고 구하기
    for col in arr_t:
        if not sum(col):
            bingo_cnt += 1
    # 대각선 (0, 0) -> (4, 4) 합 구하기
    tmp_1 = 0
    for cross_1 in range(5):
        tmp_1 += arr[cross_1][cross_1]
    if not tmp_1:
        bingo_cnt += 1
    # 대각선 (0, 4) -> (4, 0) 합 구하기
    tmp_2 = 0
    for cross_2 in range(5):
        tmp_2 += arr[cross_2][4 - cross_2]
    if not tmp_2:
        bingo_cnt += 1
    return bingo_cnt


bingo = [list(map(int, input().split())) for _ in range(5)]
announce = []
for _ in range(5):
    announce += map(int, input().split())
seq = 0
round_list = []
for num in announce:
    seq += 1
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == num:
                bingo[i][j] = 0
    if check_bingo(bingo) >= 3:  # 한 번에 빙고 개수가 두 개 이상으로 늘어나면 3을 건너 뛸 수도 있음
        break
print(seq)