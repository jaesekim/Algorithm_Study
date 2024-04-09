import sys
input = sys.stdin.readline

arr = [input().split("\n")[0] for _ in range(int(input()))]
arr = list(set(arr))
# arr.sort()
arr.sort(key=lambda x: (len(x), x))
for item in arr:
    print(item)