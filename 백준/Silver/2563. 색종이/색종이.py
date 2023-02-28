nums = int(input())
paper = set()
for _ in range(nums):
    x, y = map(int, input().split())
    for width in range(x+1, x+11):
        for height in range(y+1, y+11):
            paper.add((width, height))
print(len(paper))