def solution(n):
    answer = 0
    for divisor in range(1, n+1):
        if not n % divisor:
            answer += divisor
    return answer