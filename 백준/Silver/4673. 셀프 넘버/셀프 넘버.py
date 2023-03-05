arr = [0] * 10001
num = 1
while num <= 10000:
    if num + sum(list(map(int, list(str(num))))) <= 10000:
        arr[num + sum(list(map(int, list(str(num)))))] = 1
    num += 1
for i in range(1, len(arr)):
    if not arr[i]:
        print(i)