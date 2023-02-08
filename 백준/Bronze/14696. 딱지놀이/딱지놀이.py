def counting_pic(cnt, arr):
    counting_list = [0] * 5  # 각 그림 개수를 표현할 리스트, 인덱스 번호 == 그림 종류
    for i in range(cnt):
        counting_list[arr[i]] += 1
    return counting_list

round = int(input())
for _ in range(round):
    nbrs_a, *pics_a = map(int, input().split())  # a의 딱지 그림 수, 그림 종류 리스트
    nbrs_b, *pics_b = map(int, input().split())  # b의 딱지 그림 수, 그림 종류 리스트

    # 4: 별, 3: 동그라미, 2: 네모 1: 세모
    cnt_a = counting_pic(nbrs_a, pics_a)  # 각 그림 개수를 표현할 리스트, 인덱스 번호 == 그림 종류
    cnt_b = counting_pic(nbrs_b, pics_b)  # 각 그림 개수를 표현할 리스트

    cnt_a.reverse()  # 두 리스트를 역순으로 재배열
    cnt_b.reverse()  # 맨 앞에서부터 검사해서 큰 수 비교 용이성을 위해

    cnt_a = cnt_a[:4]
    cnt_b = cnt_b[:4]  # 0번 인덱스 부분 삭제
    
    compare = 0  # 끝까지 비교 했는지 알아보기 위한 변수

    for play in zip(cnt_a, cnt_b):
        compare += 1
        if play[0] > play[1]:
            print('A')
            break
        elif play[0] < play[1]:
            print('B')
            break
        elif compare == 4:  # 네 번 비교했는데도 승부를 못 가렸다면
            print('D')