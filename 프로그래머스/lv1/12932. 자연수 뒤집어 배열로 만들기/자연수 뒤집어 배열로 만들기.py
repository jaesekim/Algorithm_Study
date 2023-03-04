def solution(n):
    answer = []
    tmp = str(n)[::-1]
    for num in tmp:
        answer.append(int(num))
    return answer