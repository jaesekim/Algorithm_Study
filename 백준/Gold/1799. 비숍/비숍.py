import copy


def bishop(row, cnt, chess):
    global answer
    if row == N:
        answer = max(answer, cnt)
        return
    else:
        for col in range(N):
            if not right[N - 1 - row + col] and not left[row + col] and chess[row][col]:
                right[N - 1 - row + col] = 1
                left[row + col] = 1
                bishop(row, cnt+1, chess)
                right[N - 1 - row + col] = 0
                left[row + col] = 0
        bishop(row + 1, cnt, chess)
        return


def sep_chess(board, color):
    for i in range(N):
        for j in range(N):
            if color == 'w':
                if not (i + j) % 2:
                    board[i][j] = 0
            else:
                if (i + j) % 2:
                    board[i][j] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0  # 비숍을 놓을 수 있는 개수를 담아줄 변수
w_chess = copy.deepcopy(arr)
b_chess = copy.deepcopy(arr)
sep_chess(w_chess, 'w')
sep_chess(b_chess, 'b')


# 대각선 겹치는 여부
pivot = 2 * N - 1
right = [0] * pivot   # N - 1 - row + col
left = [0] * pivot    # row + col
total = 0
bishop(0, 0, w_chess)
total += answer
answer = 0
bishop(0, 0, b_chess)
total += answer
print(total)
