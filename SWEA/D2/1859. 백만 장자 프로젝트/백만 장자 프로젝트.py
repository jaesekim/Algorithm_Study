T = int(input())
for no in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))[::-1]
    # 배열 뒤집어서 계산

    profit = 0     # 총 이윤
    local_max = 0  # 로컬 최대값
    for price in lst:
        if local_max < price:
            local_max = price
        profit += local_max - price
    print(f"#{no} {profit}")