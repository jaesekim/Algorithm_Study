cnt = int(input())

num_array = list(map(int, input().split()))

length = 1
max_len = 1

i = 0

while i < len(num_array) - 1:
    if num_array[i] <= num_array[i + 1]:
        length += 1
        max_len = max(max_len, length)
    else:
        length = 1
    i += 1
i = 0
length = 1
while i < len(num_array) - 1:
    if num_array[i] >= num_array[i + 1]:
        length += 1
        max_len = max(max_len, length)
    else:
        length = 1
    i += 1
print(max_len)