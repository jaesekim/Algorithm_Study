# 절단기를 정렬

def cut_trees(h):
    total = 0
    for tree in trees:
        if tree - h > 0:
            total += tree - h
    return total


N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
height = (start + end) // 2
while start <= end:
    get = cut_trees(height)
    if M <= get:
        start = height + 1
    else:
        end = height - 1
    height = (start + end) // 2
print(height)
