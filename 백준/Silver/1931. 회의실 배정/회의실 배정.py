import sys
input = sys.stdin.readline
answer = 1
arr = []
N = int(input())
for _ in range(N):
    start, end = map(int, input().split())
    arr.append((start, end))
arr.sort(key=lambda x: (x[1], x[0]))
cur = arr[0][1]
idx = 1
while idx < N:
    if cur <= arr[idx][0]:
        cur = arr[idx][1]
        answer += 1
    idx += 1
print(answer)