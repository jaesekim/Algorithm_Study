import sys

input = sys.stdin.readline


# 로봇청소기 종료 조건 확인
def is_end(x, y, d):
    if d == 0:
        nx, ny = x + 1, y
    elif d == 1:
        nx, ny = x, y - 1
    elif d == 2:
        nx, ny = x - 1, y
    else:
        nx, ny = x, y + 1
    if not 0 <= nx < N or not 0 <= ny < M or arr[nx][ny]:
        return True
    return False


def clean_available(x, y):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        # nx, ny가 범위에 있음 + 청소하지 않았음 + 벽이 아님
        if 0 <= nx < N and 0 <= ny < M and not clean[nx][ny] and not arr[nx][ny]:
            return True
    return False


def forward_clean(x, y, d):
    if d == 0:
        nx, ny = x - 1, y
    elif d == 1:
        nx, ny = x, y + 1
    elif d == 2:
        nx, ny = x + 1, y
    else:
        nx, ny = x, y - 1
    if 0 <= nx < N and 0 <= ny < M and not arr[nx][ny] and not clean[nx][ny]:
        return True
    return False


def go_forward(x, y, d):
    if d == 0:
        return x - 1, y
    elif d == 1:
        return x, y + 1
    elif d == 2:
        return x + 1, y
    else:
        return x, y - 1


def go_backward(x, y, d):
    if d == 0:
        return x + 1, y
    elif d == 1:
        return x, y - 1
    elif d == 2:
        return x - 1, y
    else:
        return x, y + 1


N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
clean = [[0] * M for _ in range(N)]
direction = {
    0: 3,
    1: 0,
    2: 1,
    3: 2
}
answer = 0
while True:
    # 현재 칸이 아직 청소되지 않은 경우
    if not arr[r][c] and not clean[r][c]:
        answer += 1  # 청소한다
        clean[r][c] = 1  # 청소한 부분을 기록해 둔다
    if clean_available(r, c):  # 주변 중 청소되지 않은 빈칸이 있는 경우
        d = direction[d]  # 반시계방향 전환
        if forward_clean(r, c, d):  # 앞으로 전진할 수 있다면
            r, c = go_forward(r, c, d)
        continue  # 1번으로 돌아가기
    else:  # 주변 중 청소되지 않은 빈칸이 없는 경우
        if is_end(r, c, d):  # 후진 못할 때
            print(answer)
            break
        else:  # 후진 할 수 있을 때
            r, c = go_backward(r, c, d)
            continue  # 맨 처음으로 돌아가기
