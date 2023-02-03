T = int(input())

for no in range(1, T+1):
    D, A, B, F = map(int, input().split())
    print(f"#{no} {F * D/(A + B)}")