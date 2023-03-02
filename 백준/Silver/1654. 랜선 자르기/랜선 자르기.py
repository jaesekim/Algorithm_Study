def find_length(end, N):
    start = 1
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for length in stocks:
            cnt += length // mid
        if cnt >= N:
            start = mid + 1
        else:
            end = mid - 1
        # print('start:', start, 'end:', end, 'mid:', mid)
    return print(end)


K, N = map(int, input().split())
# K: 이미 가지고 있는 랜선의 개수, N: 필요한 랜선의 개수
# K <= N
stocks = [int(input()) for _ in range(K)]
find_length(max(stocks), N)