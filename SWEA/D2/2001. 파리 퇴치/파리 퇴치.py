T = int(input())

for no in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    max_count = 0
    for row in range(N-M+1):  # row 파리채 최대 갈 수 있는 곳
        for col in range(N-M+1):
            flies_count = 0
            for i in range(M):
                flies_count += sum(flies[row+i][col:col+M])
            if max_count <= flies_count:
                max_count = flies_count
    print(f"#{no} {max_count}")