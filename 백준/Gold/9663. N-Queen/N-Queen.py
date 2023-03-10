def solution(depth):
    global cnt  # 맨 아래까지 도덜하면 가능한 횟수 +1
    if depth == N:
        cnt += 1
    else:
        for idx in range(N):  # depth 행의 열방향 탐색
            col[depth] = idx  # depth 번째 행에 놓여있는 열방향 퀸 표시, 계속 초기화
            if promising(depth):   # 해당 위치가 유효하다면
                solution(depth+1)  # 다음 깊이로 넘어가기


def promising(depth):
    for i in range(depth):
        # 같은 열이거나 대각선에 겹치는 부분이 있으면 False
        # col[depth] 현재 깊이보다 작은 깊이에서 같은 값이 나오면 겹친다는 의미
        # depth & i -> row / col[depth] & col[i] -> column
        if col[depth] == col[i] or abs(col[depth] - col[i]) == abs(depth - i):
            return 0
    return 1


N = int(input())
col = [0] * N
cnt = 0
solution(0)
print(cnt)