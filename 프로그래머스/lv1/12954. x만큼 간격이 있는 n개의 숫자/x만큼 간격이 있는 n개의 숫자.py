def solution(x, n):
    answer = []
    add = x
    for _ in range(n):
        answer.append(x)
        x += add
    return answer