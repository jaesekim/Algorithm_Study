from itertools import combinations


def check_escape(x, y, N, arr):
    # row 검사
    k = 0
    while y + k < N and (x, y + k) not in arr:
        if (x, y + k) in teacher:
            return 0
        k += 1

    k = 0
    while y - k >= 0 and (x, y - k) not in arr:
        if (x, y - k) in teacher:
            return 0
        k += 1

    # col 검사
    k = 0
    while x + k < N and (x + k, y) not in arr:
        if (x + k, y) in teacher:
            return 0
        k += 1

    k = 0
    while x - k >= 0 and (x - k, y) not in arr:
        if (x - k, y) in teacher:
            return 0
        k += 1
    return 1


def solution(N):
    for obstacle in obstacles:
        cnt = 0                     # 탈출이 유효한 학생 수
        for point in student:
            if not check_escape(point[0], point[1], N, obstacle):  # 탈출이 유효하지 않다면
                break               # 다음 장애물 반복문으로
            else:
                cnt += 1            # 해당 학생의 탈출이 유효하다면 cnt += 1
        if cnt == len(student):
            return print("YES")
    return print("NO")


N = int(input())
aisle = [input().split() for _ in range(N)]
coordinates = [(i, j) for i in range(N) for j in range(N) if aisle[i][j] == 'X']  # 장애물을 놓을 수 있는 좌표
student = [(i, j) for i in range(N) for j in range(N) if aisle[i][j] == 'S']      # 학생의 좌표
teacher = [(i, j) for i in range(N) for j in range(N) if aisle[i][j] == 'T']      # 선생의 좌표
obstacles = list(map(list, combinations(coordinates, 3)))                         # 가능한 조합의 가지 수를 리스트에 넣기
solution(N)