import copy

start = int(input())
num = copy.deepcopy(start)
max_arr = 0
for num in range(start, -1, -1):
    arr = [start]
    while True:
        arr.append(num)
        num = arr[-2] - arr[-1]
        if arr[-1] < 0:
            arr.pop()
            break
    if len(arr) >= max_arr:
        max_arr = len(arr)
        answer = copy.deepcopy(arr)
print(max_arr)
print(*answer)