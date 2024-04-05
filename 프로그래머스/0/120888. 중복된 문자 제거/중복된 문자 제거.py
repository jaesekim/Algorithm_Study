def solution(my_string):
    answer = ''
    for char in my_string:
        if char in answer:
            continue
        answer += char
    return answer