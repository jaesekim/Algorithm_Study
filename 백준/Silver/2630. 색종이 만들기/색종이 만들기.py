import sys
input = sys.stdin.readline


def all_white_blue(i, j, n):
    global white
    global blue
    valid = 0
    for r in range(i, i + n):
        valid += sum(paper[r][j:j + n])
    if valid == 0:
        white += 1
        return True
    elif valid == n * n:
        blue += 1
        return True
    return False


def validation(i, j, n):
    global white
    global blue
    if n == 1:
        if paper[i][j]:
            blue += 1
        else:
            white += 1
        return
    elif all_white_blue(i, j, n):
        return
    else:
        validation(i, j, n // 2)
        validation(i + n // 2, j, n // 2)
        validation(i, j + n // 2, n // 2)
        validation(i + n // 2, j + n // 2, n // 2)


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0
validation(0, 0, N)
print(white)
print(blue)
