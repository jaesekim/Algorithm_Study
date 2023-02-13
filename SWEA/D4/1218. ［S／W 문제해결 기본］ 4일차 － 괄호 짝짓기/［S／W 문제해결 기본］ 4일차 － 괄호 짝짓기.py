for no in range(1, 11):
    N = int(input())
    chars = input()
    stack = []
    for i in range(len(chars)):
        if chars[i] not in '\(\)\{\}\<\>\[\]':
            continue
        if len(stack) and stack[-1] == '(' and chars[i] == ')':
            stack.pop()
        elif len(stack) and stack[-1] == '{' and chars[i] == '}':
            stack.pop()
        elif len(stack) and stack[-1] == '[' and chars[i] == ']':
            stack.pop()
        elif len(stack) and stack[-1] == '<' and chars[i] == '>':
            stack.pop()
        else:
            stack.append(chars[i])
    if not len(stack):
        print(f"#{no} {1}")
    else:
        print(f"#{no} {0}")