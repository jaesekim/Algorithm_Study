def backtracking(row, mul, n):
    """
    :param row: 현재 보고 있는 row
    :param mul: 곱셈의 결과
    :param n: n x n matrix
    """
    global ans
    if row == n:
        ans = mul
        return
    for col in range(n):
        tmp = mul * arr[row][col]
        if not check_col[col] and ans < tmp:
            check_col[col] = 1
            backtracking(row+1, tmp, n)
            check_col[col] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] /= 100
    check_col = [0] * N
    ans = 0
    backtracking(0, 1, N)
    print(f"#{tc} {format(ans * 100, '.6f')}")