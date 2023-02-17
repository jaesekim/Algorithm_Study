for no in range(1, 11):
    length, chars = input().split()
    stack = []
    for i in range(int(length)):
        if not stack or stack[-1] != chars[i]:
            stack.append(chars[i])
        else:
            stack.pop()
    answer = ''
    for char in stack:
        answer += char
    print(f"#{no} {answer}")