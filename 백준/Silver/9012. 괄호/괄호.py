for _ in range(int(input())):
    parenthesis = input()
    stack = []
    for char in parenthesis:
        if char == ")" and stack:
            stack.pop()
        elif char == ")" and not stack:
            stack.append(")")
            break
        else:
            stack.append(char)
    if stack:
        print("NO")
    else:
        print("YES")