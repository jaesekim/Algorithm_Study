def count_one(chars):
    mx_cnt = 0
    for char in chars:
        cnt = 0
        for num in char:
            if num == 1:
                cnt += 1
                if cnt > mx_cnt:
                    mx_cnt = cnt
            else:
                cnt = 0
    return mx_cnt


T = int(input())
for no in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_t = list(map(list, zip(*arr)))  # 전치행렬 만들기

    arr_cnt = count_one(arr)
    arr_t_cnt = count_one(arr_t)
    mx_value = max(arr_cnt, arr_t_cnt)

    print(f"#{no} {mx_value}")