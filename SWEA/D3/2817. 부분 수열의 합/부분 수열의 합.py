def mk_subsets(length, k):
    cnt = 0
    for i in range(1 << length):  # 2^length 와 같은 의미
        tmp = []
        for j in range(length):
            if i & (1 << j):  # 비트 and: 열의 모든 비트가 1이면 결과 1, 나머지 0
                tmp.append(arr[j])
        if sum(tmp) == k:
            cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    subsets = []
    print(f"#{tc} {mk_subsets(N, K)}")
