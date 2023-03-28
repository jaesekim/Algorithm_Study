def recursive(i, cnt):  # i: 바꿀 시작 index, cnt: 현재까지 바꾼 횟수, ex: 바꿀 수 있는 최대 횟수
    global answer
    if cnt == exchange:
        tmp = int("".join(list(map(str, num))))
        if answer <= tmp:
            answer = tmp
            return
    # 인덱스 맨 끝까지 왔는 데 cnt 아직 exchange 만큼 다 안 갔을 때
    # 이미 정렬은 끝난 것
    if i == length - 1:
        if flag:  # 중복되는 값이 있다면
            tmp = int("".join(list(map(str, num))))
            if answer <= tmp:
                answer = tmp
                return
        elif (exchange - cnt) % 2:
            num[-2], num[-1] = num[-1], num[-2]
            tmp = int("".join(list(map(str, num))))
            if answer <= tmp:
                answer = tmp
                return
        elif not (exchange - cnt) % 2:
            tmp = int("".join(list(map(str, num))))
            if answer <= tmp:
                answer = tmp
                return
    mx_num = max(num[i:])
    if num[i] == mx_num:  # 지금 참조하는 인덱스가 최대값이면 다음 재귀로 넘어간다
        recursive(i+1, cnt)
    else:  # 지금 참조하는 인덱스 값이 최대가 아니라면
        for j in range(i+1, length):
            if num[j] == mx_num:
                num[i], num[j] = num[j], num[i]
                recursive(i+1, cnt+1)
                num[i], num[j] = num[j], num[i]


T = int(input())
for tc in range(1, T+1):
    num, exchange = map(int, input().split())
    num = list(map(int, list(str(num))))
    length = len(num)
    answer = 0
    flag = 0  # 중복된 숫자 있는지 판별하는 변수
    num_nums = [0] * 10
    for i in num:
        num_nums[i] += 1
    if max(num_nums) >= 2:
        flag = 1
    recursive(0, 0)
    print(f"#{tc} {answer}")
