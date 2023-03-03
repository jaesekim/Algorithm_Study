T = int(input())

for test_no in range(1, T+1):
    N = int(input())
    farm = [list(map(int, list(input()))) for _ in range(N)]
    times = N // 2 + 1  # 반복 돌릴 수
    mid = (N - 1) // 2  # 행렬의 중간 행 위치
    answer = 0          # 정답을 담아줄 변수
    for i in range(times):
        if not i:   # 첫 루프일 때
            answer += sum(farm[mid])
            N -= 2
            continue
        answer += sum(farm[mid-i][i:i+N])
        answer += sum(farm[mid+i][i:i+N])
        N -= 2
    print(f"#{test_no} {answer}")