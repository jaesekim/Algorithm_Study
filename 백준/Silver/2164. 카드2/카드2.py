import collections

N = int(input())
queue = collections.deque()
for num in range(1, N+1):
    queue.append(num)
while True:
    if len(queue) == 1:
        break
    queue.popleft()
    first = queue.popleft()
    queue.append(first)
print(queue[0])
