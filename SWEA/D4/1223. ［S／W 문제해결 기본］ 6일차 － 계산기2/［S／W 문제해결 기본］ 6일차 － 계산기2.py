for no in range(1, 11):
    length = int(input())
    cal = input()
    result = ''  # 후위 연산으로 바꾼 결과값을 넣을 빈 문자열
    stack = []   # 스택을 위한 리스트
    for i in range(length):
        if cal[i].isdigit():
            result += cal[i]
        # 1. stack 비어있을 때
        # 2. 새로 들어올 연산자 우선순위 > 스택 맨 위 연산자 우선순위
        elif not stack or cal[i] == '*' and stack[-1] == '+':
            stack.append(cal[i])
        # 1. 새로 스택에 들어올 연산자의 우선순위 == 스택 맨 위에 있는 연산자의 우선순위
        # 2. 새로 들어올 연산자의 우선순위 < 스택 맨 위에 있는 연산자의 우선순위
        # -> stack.pop()을 먼저 한 뒤 새로 들어올 것 append()
        else:
            result += stack.pop()
            stack.append(cal[i])

    # stack 남은 연산자 모두 추가해주기
    while stack:
        result += stack.pop()
    # 후위 표기식으로 된 것들 연산
    for char in result:  # result 맨 앞 부터 참조하면서 계산
        if char.isdigit():  # 숫자면 스택에 바로 쌓기
            stack.append(char)
        else:  # 연산자라면
            x1 = int(stack.pop())
            x2 = int(stack.pop())
            if char == '*':
                stack.append(x1 * x2)
            else:
                stack.append(x1 + x2)
    answer = stack[-1]
    print(f"#{no} {answer}")