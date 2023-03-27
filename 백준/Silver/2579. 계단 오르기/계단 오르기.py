nums = int(input())
stairs = []
dp = []
for _ in range(nums):
    stairs.append(int(input()))
if nums <= 2:
    print(sum(stairs))
else:
    # 계단 1일때 최대값
    dp.append(stairs[0])
    # 계단 2일때 최대값
    dp.append(stairs[0] + stairs[1])
    # 계단 3일때 최대값
    dp.append(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))
    for i in range(3, nums):
        # 현재 계단 index: i
        # 1. i-1 번째 계단을 밟았다면 i-3 까지의 최대값 필요
        # 2. i-2 번째 계단을 밟고 두 칸 건너 뛰기
        dp.append(max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i]))
    print(dp[-1])
