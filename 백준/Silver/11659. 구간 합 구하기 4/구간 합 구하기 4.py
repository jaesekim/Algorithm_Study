import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_arr = list(map(int, input().split()))
cumulative_sum = [0]
cumulative = 0
for num in num_arr:
    cumulative += num
    cumulative_sum.append(cumulative)

for _ in range(M):
    i, j = map(int, input().split())
    print(cumulative_sum[j] - cumulative_sum[i - 1])