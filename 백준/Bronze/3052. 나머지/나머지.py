remainderSet = set()

for _ in range(10):
    num = int(input())
    remainderSet.add(num % 42)
print(len(remainderSet))