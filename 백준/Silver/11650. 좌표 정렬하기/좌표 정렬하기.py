N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
for item in arr:
    print(*item)