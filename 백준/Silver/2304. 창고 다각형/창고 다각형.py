N = int(input())
column = []
for _ in range(N):
    column.append(tuple(map(int, input().split())))
x_lst = []  # x좌표 가장 큰 값을 저장하기 위한 변수
for col in column:
    x_lst.append(col[0])
warehouse = [0] * (max(x_lst) + 1)
# x좌표, 인덱스 맞춰주기 위해 + 1
# warehouse: 철근의 위치와 높이를 담아줄 리스트 변수
for point, height in column:
    warehouse[point] = height

mx_idx = warehouse.index(max(warehouse))  # 가장 높은 값을 가지고 있는 인덱스(위치)
left = 0                                  # 왼쪽 포인터
right = len(warehouse) - 1                # 오른쪽 포인터

# 왼쪽 검사
local_left_max = 0
while left < mx_idx:
    if warehouse[left] > local_left_max:
        local_left_max = warehouse[left]
    else:
        warehouse[left] = local_left_max
    left += 1

# 오른쪽 검사
local_right_max = 0
while right > mx_idx:
    if warehouse[right] > local_right_max:
        local_right_max = warehouse[right]
    else:
        warehouse[right] = local_right_max
    right -= 1
print(sum(warehouse))