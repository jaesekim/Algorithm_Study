def total_sum(arr):
    result = 0
    for i in arr:
        result += i
    return result


for _ in range(10):
    no = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_value = 0
    
    # 가로
    for horizen in arr:
        dummy_hor = total_sum(horizen)
        if dummy_hor >= max_value:
            max_value = dummy_hor
    
    # 세로
    for i in range(100):
        dummy_arr = 0
        for j in range(100):
            dummy_arr += arr[j][i]
        if dummy_arr >= max_value:
            max_value = dummy_arr
    
    # 0, 0 - > 99, 99 대각선
    dummy_cross1 = 0
    for x in range(100):
        dummy_cross1 += arr[x][x]
    if dummy_cross1 >= max_value:
            max_value = dummy_cross1
    
    # 0, 99 -> 99, 0 대각선
    dummy_cross2 = 0
    for y in range(100):
        dummy_cross2 += arr[y][99-y]
    if dummy_cross2 >= max_value:
            max_value = dummy_cross2

    print(f"#{no} {max_value}")