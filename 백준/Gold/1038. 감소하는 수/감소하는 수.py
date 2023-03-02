import itertools as it


def descending(n):
    if n > 1022:
        return print(-1)
    desc_comb = []
    for digit in range(1, 11):
        for comb in list(map(list, it.combinations(range(0, 10), digit))):
            comb.sort(reverse=True)  # 내림차순으로 일단 만들기
            desc_comb.append(int(''.join(map(str, comb))))
    desc_comb.sort()
    return print(desc_comb[n])


descending(int(input()))