N, K = map(int, input().split())
arr = list(map(int, input().split()))
local_add = 0
# 인덱스 0 ~ K - 1 까지 값을 넣어준다
# 첫 구간의 합을 미리 구해준다
for i in range(K):
    local_add += arr[i]
mx_list = [local_add]
i = 0
while i < N - K:
    local_add = local_add - arr[i] + arr[i+K]
    mx_list.append(local_add)
    i += 1
print(max(mx_list))