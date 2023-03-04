import itertools


def find_100(arrs):
    for comb in arrs:
        if sum(comb) == 100:
            return comb 


heights = []
for _ in range(9):
    heights.append(int(input()))

combs = sorted(find_100(list(map(list, itertools.combinations(heights, 7)))))
for x in combs:
    print(x)