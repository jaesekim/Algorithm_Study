T = int(input())

for no in range(1, T+1):
    st = input()
    ans = cnt = 0
    # ans: 잘린 막대기 수
    # cnt: 잘릴 수 있는 막대기 수
    for i in range(len(st)):
        if st[i] == '(':    # 막대기 시작 또는 레이저
            cnt += 1  # 일단 레이저/막대기 판단 유보
        else:   # )
            if st[i - 1] == '(':    # 레이저
                cnt -= 1  # 잘릴 수 있는 막대기가 아니니까 하나 줄여주고
                ans += cnt  
                # 이전에 나왔던 막대기들이 잘린 것이니까 cnt만큼 늘려준다
                # 막대기 왼쪽 뭉텅이
            else:  # 레이저가 아닌 것 -> 막대기의 끝
                cnt -= 1  # 잘릴 수 있는 막대기 수 하나 줄여주고
                ans += 1  # 레이저로 잘린 오른쪽 뭉텅이 하나 추가
    print(f"#{no} {ans}")