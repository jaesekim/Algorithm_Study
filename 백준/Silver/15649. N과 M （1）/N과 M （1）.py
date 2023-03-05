import itertools

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
comb = list(map(list, itertools.permutations(arr, M)))
for value in comb:
    print(*value)