def backtracking(depth):
    global answer
    if depth == N:
        answer += 1
        return
    for idx in range(N):
        if not check_col[idx] and not diagonal_left[idx + depth] and not diagonal_right[N - 1 + idx - depth]:
            check_col[idx] = 1
            diagonal_left[idx + depth] = 1
            diagonal_right[N - 1 + idx - depth] = 1

            backtracking(depth + 1)

            check_col[idx] = 0
            diagonal_left[idx + depth] = 0
            diagonal_right[N - 1 + idx - depth] = 0



N = int(input())
check_col = [0] * N
diagonal_right = [0] * (2 * N - 1)
diagonal_left = [0] * (2 * N - 1)
answer = 0
backtracking(0)
print(answer)