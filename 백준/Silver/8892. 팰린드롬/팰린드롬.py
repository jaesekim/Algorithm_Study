from itertools import permutations


def validation(w):
    i = 0
    while i < len(w) // 2:
        if w[i] != w[len(w) - i - 1]:
            return False
        i += 1
    return True


for _ in range(int(input())):
    words = []
    flag = 0
    for _ in range(int(input())):
        words.append(input())
    perm = list(permutations(words, 2))
    for item in perm:
        if validation(item[0] + item[1]):
            print(item[0] + item[1])
            flag = 1
            break
    if not flag:
        print(0)
