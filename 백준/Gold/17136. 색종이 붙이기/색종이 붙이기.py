def check_zero(x, y, n):
    """
    arr[x][y] 지점부터 n x n 색종이로 가릴 수 있는지 여부 확인
    0이 하나라도 껴 있다면 1(True)반환
    """
    for i in range(x, x+n):
        for j in range(y, y+n):
            if not arr[i][j]:  # 0이 껴 있다면
                return 1
    return 0


def convert_one_to_zero(x, y, n):
    """
    색종이로 덮은 부분 0으로 바꾸는 함수
    """
    for i in range(x, x+n):
        for j in range(y, y+n):
            arr[i][j] = 0
    return

def recover_arr(x, y, n):
    """
    1 -> 0 으로 바꿨던 것 다시 원상복구
    """
    for i in range(x, x+n):
        for j in range(y, y+n):
            arr[i][j] = 1
    return


def solution():
    global cnt
    # arr 1차원리스트로 다 만들기, 1이 아예 없다면
    # sum(paper) == 25 부터 시작
    if 1 not in sum(arr, []):
        cnt = min(cnt, 26 - sum(paper))
        return  # 더 이상 가릴 1이 없으니까 바로 함수 종료
    # 10 x 10 matrix 모든 인덱스 체크
    for i in range(10):
        for j in range(10):
            # 가릴 부분이 없다면
            if not arr[i][j]:
                continue  # 다음 인덱스로
            for k in range(5, 0, -1):  # 5 x 5 색종이부터 비교
                # 인덱스 범위를 벗어났다면, k x k 색종이를 다 썼다면, check 함수 True
                if i + k > 10 or j + k > 10:
                    continue
                if not paper[k] or check_zero(i, j, k):
                    continue  # 그 다음으로 큰 색종이 탐색
                # 모든 예외상황에서 빠져나왔다면
                paper[k] -= 1  # 해당 크기 색종이 개수 하나 줄이기
                convert_one_to_zero(i, j, k)  # 덮은 부분 0으로 바꿔주기
                solution()  # 재귀 호출
                paper[k] += 1  # 색종이 개수 원상복귀
                recover_arr(i, j, k)
            return


arr = [list(map(int, input().split())) for _ in range(10)]
paper = [0, 5, 5, 5, 5, 5]  # 색종이 개수 확인용
cnt = 26  # 최대 25장
solution()
if cnt == 26:
    print(-1)
else:
    print(cnt-1)