def side_nbr(index):
    """

    :param index: 인덱스를 튜플로 받음
    :return: 나머지 인덱스 반환
    """
    if index == (0, 5) or index == (5, 0):
        return [1, 2, 3, 4]
    elif index == (1, 3) or index == (3, 1):
        return [0, 2, 4, 5]
    else:
        return [0, 1, 3, 5]


N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]
idx_dict = {
    0: 5,
    1: 3,
    2: 4,
    3: 1,
    4: 2,
    5: 0
}  # 주사위 반대쪽에 있는 인덱스끼리 묶어준 딕셔너리
mx_list = []  # 바닥 별로 최대값을 담아줄 리스트
for floor in range(6):  # 첫번째 주사위 바닥에 위치할 숫자의 번호 인덱스
    mx_value = 0  # 주사위 옆면 최대 합을 더해줄 변수
    top = idx_dict[floor]  # 주사위 위쪽의 인덱스
    # dice[0]: 첫 번째 주사위 / idx_dict[floor] 주사위 바닥의 반대편 숫자
    # top: 첫번째 주사위의 맨 위 숫자
    side_max = [dices[0][i] for i in side_nbr((floor, top))]
    # 첫번째 주사위의 옆면 값을 리스트에 담아준다.
    mx_value += max(side_max)
    for num in range(1, N):  # num: 입력받은 주사위의 두번째 주사위부터 N번째 주사위를 찾기위한 변수
        floor_idx = dices[num].index(dices[num-1][top])
        # print(dices[num][dices[num].index(dices[num-1][top])])
        top = idx_dict[floor_idx]
        side_max = [dices[num][i] for i in side_nbr((floor_idx, top))]
        mx_value += max(side_max)
    mx_list.append(mx_value)
print(max(mx_list))