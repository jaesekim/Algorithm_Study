height, width = map(int, input().split())
arr = list(map(int, input().split()))
mx_idx = arr.index(max(arr))
water = 0  # 고인 물

# 왼쪽부터 검사
left_local_max = arr[0]
left = 0
while left < mx_idx:
    if arr[left] <= left_local_max:
        water += left_local_max - arr[left]
    else:
        left_local_max = arr[left]
    left += 1
# 오른쪽부터 검사
right_local_max = arr[-1]
right = width - 1
while right > mx_idx:
    if arr[right] <= right_local_max:
        water += right_local_max - arr[right]
    else:
        right_local_max = arr[right]
    right -= 1
print(water)
