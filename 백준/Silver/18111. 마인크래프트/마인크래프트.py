N, M, B = map(int, input().split())
# 제거: 2초 / 놓기: 1초
arr = []
for _ in range(N):  # 1차원 리스트로 받기
    arr += list(map(int, input().split()))
mn_floor = min(arr)
mx_floor = max(arr)
min_time = 1e9
for floor in range(mn_floor, mx_floor+1):  # 평탄화 할 층
    time = 0
    block = B
    for i in range(N * M):
        if arr[i] == floor:
            continue
        elif floor < arr[i]:
            time += 2 * (arr[i] - floor)
            block += (arr[i] - floor)
        else:
            time += (floor - arr[i])
            block -= (floor - arr[i])
    if block >= 0 and time <= min_time:
        min_time = time
        min_floor = floor
print(min_time, min_floor)