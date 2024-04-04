import sys
input = sys.stdin.readline

stack = []
for _ in range(int(input())):
    money = int(input())
    if not money:
        stack.pop()
    else:
        stack.append(money)
print(sum(stack))
