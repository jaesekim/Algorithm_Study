# 후위 표기법을 계산하는 함수를 만들어보자
def calculate(postfix):
    stack = []
    for k in postfix:  # 후위표기법 내의 요소를 도는 반복문(인덱스 0부터)
        #print(type(k))
        if k == '+':
            stack.append(stack.pop() + stack.pop())
        elif k == '-':
            stack.append(stack.pop() - stack.pop())
        elif k == '*':
            stack.append(stack.pop() * stack.pop())
        elif k == '/':
            rv = stack.pop()
            stack.append(stack.pop() / rv)
        else:
            stack.append(int(k))
    return stack.pop()

# 후위 표기법으로 바꿔주자
for t in range(1, 11):
    n = int(input())  # 테케 길이
    infix = input()  # 중위표기법 받기
    #print(infix)
    stack = []
    postfix = ''  # 후위표기법 저장
    #print(lst)
    for i in infix:
        if i == '*': #or i == '/':
            while stack and stack[-1] == '*':  #or stack[-1] == '/':
                postfix += stack.pop()
            stack += i
        elif i == '+': # 괄호 안에 있는 덧셈이면 괄호가 있을 때 여는 괄호가 나올 때 까지 팝.
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack += i
        elif i == '(':
            stack += i
        elif i == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:  # n이 숫자일 때
            postfix += i
    while stack:
        postfix += stack.pop()
    #print(postfix)


    print(f'#{t} {calculate(postfix)}')