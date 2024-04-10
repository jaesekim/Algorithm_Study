import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = []
count = 0
for _ in range(N):
    coin.append(int(input()))
for element in coin[::-1]:
    if K < element:
        continue
    count += K // element
    K %= element
    if not K:
        break
print(count)
