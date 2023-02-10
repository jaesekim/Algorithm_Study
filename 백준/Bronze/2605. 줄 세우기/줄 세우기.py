students = int(input())
vote = list(map(int, input().split()))
queue = []
for idx, seq in enumerate(vote):
    queue.insert(idx - seq, idx+1)
print(*queue)