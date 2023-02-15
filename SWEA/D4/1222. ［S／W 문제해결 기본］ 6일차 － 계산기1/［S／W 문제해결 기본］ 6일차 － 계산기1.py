for no in range(1, 11):
    length = int(input())
    calculate = input()
    stack = []
    num_stack = []
    result = ''
    answer = 0
    for i in range(length):
        if calculate[i].isdecimal():
            result += calculate[i]
        else:
            stack.append(calculate[i])
    # 연산자 후위에 모두 붙여주기

    for _ in range(len(stack)):
        result += stack.pop()

    # 계산
    for char in result:
        if char.isdecimal():
            stack.append(int(char))
        else:
            x = stack.pop()
            y = stack.pop()
            stack.append(x + y)
    print(f'#{no} {stack[-1]}')