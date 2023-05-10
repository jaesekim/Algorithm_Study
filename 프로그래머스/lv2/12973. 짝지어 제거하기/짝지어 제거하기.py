from collections import deque


def solution(s):
    stack = deque()
    for char in s:
        if not stack or stack[-1] != char:  # stack 비어있거나 stack 맨 위 값과 현재 값 같지 않다면
            stack.append(char)
        else:  # stack 맨 위 값과 현재 값이 같다면
            stack.pop()
    if stack:
        return 0
    return 1