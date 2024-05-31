N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer = 0

A.sort()
B.sort(reverse=True)

for idx in range(N):
    answer += (A[idx] * B[idx])

print(answer)