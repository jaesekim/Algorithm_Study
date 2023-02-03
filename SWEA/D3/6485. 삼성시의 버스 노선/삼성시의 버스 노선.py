T = int(input())

for no in range(1, T+1):
    N = int(input())
    stop = [0] * 5001  # 인덱스랑 정류장 맞춰주기 위해서
    for i in range(N):
        a, b = map(int, input().split())
        for j in range(a, b+1):
            stop[j] += 1
    base = []
    for x in range(int(input())):
        index = int(input())
        base.append(stop[index])
    print(f"#{no}", *base)