# 하 우 상 좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def find_target():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == target:
                print(i + 1, j + 1)
                return


N = int(input())
target = int(input())
arr = [[0] * N for _ in range(N)]
num = N ** 2
x, y, idx = -1, 0, 0
# 초기값 0, -1 시작함으로써 연산을 편하게 한다.
while num >= 1:
    nx, ny = x + dx[idx], y + dy[idx]  # 다음에 찍을 것 정해주기
    if 0 <= nx < N and 0 <= ny < N and not arr[nx][ny]:  # 작성할 수 있는 범위 지정
        arr[nx][ny] = num  # 값 넣어주기
        num -= 1  # num 1 늘려주기
        x, y = nx, ny  # x, y 값 갱신
    else:  # num 넣어줄 수 없는 좌표라면
        idx = (idx + 1) % 4
for chars in arr:
    print(*chars)
find_target()
