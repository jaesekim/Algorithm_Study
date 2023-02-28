N = int(input())
names = []
for _ in range(N):
    names.append(input().split())
answer = sorted(names, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for name in answer:
    print(name[0])