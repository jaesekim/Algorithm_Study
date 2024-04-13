from collections import deque


def answer_print(chars):
    answer = "["
    for idx in range(len(chars)):
        if idx != len(chars) - 1:
            answer += str(chars[idx]) + ","
        else:
            answer += str(chars[idx])
    return answer + "]"


for _ in range(int(input())):
    p = input()
    n = int(input())
    queue = deque()
    left = True
    flag = 0
    arr = input().lstrip("[").rstrip("]")
    if not arr:
        queue = deque([])
    else:
        queue = deque(list(map(int, arr.split(","))))
    for command in p:
        if command == "R":
            left = not left
        else:  # pop 요청
            if not queue:
                flag = 1
                break
            if left:  # 현재 포인터가 왼쪽이라면
                queue.popleft()
            else:  # 현재 포인터가 오른쪽이라면
                queue.pop()
    if queue and left:
        print(answer_print(list(queue)))
    elif queue and not left:
        print(answer_print(list(queue)[::-1]))
    elif not flag:
        print([])
    else:
        print("error")
