N, M = map(int, input().split())
name_set1 = set()
name_set2 = set()

for _ in range(N):
    name_set1.add(input())
for _ in range(M):
    name_set2.add(input())

intersection = list(name_set1 & name_set2)
intersection.sort()
print(len(intersection))
for i in intersection:
    print(i)