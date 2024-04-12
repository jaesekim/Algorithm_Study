def validation(start, end, word):
    while start < end:
        if word[start] != word[end]:
            return [start, end, False]
        start += 1
        end -= 1
    return [start, end, True]


T = int(input())
for _ in range(T):
    chars = input().rstrip()
    left, right, answer = 0, len(chars) - 1, 0

    s, e, status = validation(left, right, chars)
    if status:
        answer = 0
    else:
        if validation(s+1, e, chars)[2] or validation(s, e-1, chars)[2]:
            answer = 1
        else:
            answer = 2
    print(answer)