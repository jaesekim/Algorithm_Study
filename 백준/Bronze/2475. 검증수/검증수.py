arr = list(map(int, input().split()))
answer = 0
for num in arr:
    answer += num ** 2
print(answer % 10)