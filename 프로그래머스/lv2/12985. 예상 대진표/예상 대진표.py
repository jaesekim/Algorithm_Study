import copy


def solution(n, a, b):
    answer = 0
    start = 1
    end = copy.deepcopy(n)
    while n > 1:
        answer += 1
        n //= 2
    print(answer)
    while start <= end:
        mid = (start + end) // 2
        if a <= mid < b or b <= mid < a:
            return answer
        else:
            answer -= 1
            if a <= mid:
                end = mid
            else:
                start = mid + 1

