# 최대 상금
def recursive(i, cnt):  
    # i: 비교하려는 인덱스. 맨 처음 인덱스부터 시작한다. 
    # -> 최대값 맨 앞부터 채우기 위함
    if cnt == swap:  # 스왑 횟수 모두 채웠다면
        answer.append(int("".join(list(map(str, num)))))
        return
    
    # cnt가 swap 만큼 다 돌기전에 마지막 인덱스에 도달했다면 
    # -> 이미 정렬은 끝난 것
    if i == length - 1:
        if (swap - cnt) % 2 and not flag:
            num[-2], num[-1] = num[-1], num[-2]  # 맨 마지막 두 개 스왑
        answer.append(int("".join(list(map(str, num)))))
        return
    local_mx = max(num[i:])
    # 최대값이 현재 비교할 인덱스에 있는 값과 동일하다면 그리디 관점에서
    # 이미 최대값을 이루고 있다는 의미이므로 그 다음 인덱스로 넘어가기
    if num[i] == local_mx:
        recursive(i+1, cnt)
    else:  # i번째 인덱스 값이 local_mx가 아니라면
        # i보다 큰 인덱스 중에 local_mx가 어디에 있는지 찾는 것이다
        for j in range(i+1, length):
            if num[j] == local_mx:
                num[i], num[j] = num[j], num[i]
                recursive(i+1, cnt+1)  # 다음 비교 인덱스, 스왑했으니까 +1
                num[i], num[j] = num[j], num[i]

T = int(input())
for tc in range(1, T+1):
    num, swap = input().split()  # swap: 반복해야하는 횟수
    swap = int(swap)
    num = list(map(int, list(num)))
    length = len(num)
    answer = []
    flag = 0  # 중복된 숫자가 있는지 확인하기 위한 변수. 0: 없음, 1: 있음
    num_cnt = [0] * 10
    for k in num:
        num_cnt[k] += 1
    if max(num_cnt) >= 2:
        flag = 1
    recursive(0, 0)
    print(f"#{tc} {max(answer)}")