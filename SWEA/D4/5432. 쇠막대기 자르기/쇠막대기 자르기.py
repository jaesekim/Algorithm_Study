T = int(input())

for no in range(1, T+1):
    st = input()
    ans = cnt = 0
    for i in range(len(st)):
        if st[i] == '(':    # 막대기 시작 또는 레이저
            cnt += 1
        else:   # )
            if st[i - 1] == '(':    # 레이저
                cnt -= 1
                ans += cnt
            else:
                cnt -= 1
                ans += 1
    print(f"#{no} {ans}")