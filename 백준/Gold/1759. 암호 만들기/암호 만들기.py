def consonants_vowels(lst):
    cnt = 0
    length = len(lst)
    for char in lst:
        if char in vowel:
            cnt += 1
    if cnt >= 1 and length - cnt >= 2:
        return 1
    return 0


def comb(n, r):
    if not r:
        if consonants_vowels(subset):
            answer.append(''.join(sorted(subset)))
    elif n < r:
        return
    else:
        subset[r - 1] = alphabets[n - 1]
        comb(n - 1, r - 1)
        comb(n - 1, r)


L, C = map(int, input().split())
alphabets = input().split()
vowel = ['a', 'e', 'i', 'o', 'u']
subset = [0] * L
answer = []
comb(C, L)
answer.sort()
for dic in answer:
    print(dic)
