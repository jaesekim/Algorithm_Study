import copy

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    times = copy.deepcopy(N)
    denominator = 1   # 분모
    numerator = 1     # 분자
    for _ in range(N):
        numerator *= M
        denominator *= N
        M -= 1
        N -= 1
    print(numerator // denominator)