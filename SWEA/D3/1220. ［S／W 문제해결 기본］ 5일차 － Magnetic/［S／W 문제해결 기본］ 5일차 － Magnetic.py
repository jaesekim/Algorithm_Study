for test_no in range(1, 11):
    # 1: N극  2: S 극
    N = int(input())
    arr = [input().split() for _ in range(N)]
    arr_t = list(map(list, zip(*arr)))  # 전치 행렬 만들기 / 왼쪽 N극 오른쪽 S극
    cnt = 0
    for lst in arr_t:
        answer = ''
        for char in lst:
            if char != '0':
                answer += char
        for i in range(len(answer) - 1):
            if answer[i:i+2] == '12':
                cnt += 1
    print(f"#{test_no} {cnt}")