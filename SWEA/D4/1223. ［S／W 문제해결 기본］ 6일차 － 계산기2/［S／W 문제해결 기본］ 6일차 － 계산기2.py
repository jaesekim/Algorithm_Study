"""
1. 후위 표기식으로 바꾸기/ 숫자는 문자열에 쌓고 연산자는 스택에
우선 순위의 연산자가 스택의 상단에 있어야 한다.
동일 순위를 만났을 때 스택 내의 연산자 pop하고 문자열에 넣고 만난 연산자 스택에 넣기
끝까지 돌았을 때 스택 안의 연산자 문자열에 넣기
2. 후위 표기법 계산하기 / 문자열 0번째 인덱스부터 스택에 넣어주면서 연산자 만나면 두 번 팝해서
계산하기. 이때 두번째 팝한 숫자,연산자,첫번째 팝한 숫자 순서
"""
# 후위 표기법을 계산하는 함수를 만들어보자
def calculate(postfix):
    stack = []
    for k in postfix:  # 후위표기법 내의 요소를 도는 반복문(인덱스 0부터)
        #print(type(k))
        #print(stack)
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
        elif i == '+': # 더하기는 그냥 스택에 무언가 있을 때 하나 팝하기만 하기
            while stack:
                postfix += stack.pop()
            stack += i
        else:  # n이 숫자일 때
            postfix += i
    while stack:
        postfix += stack.pop()


    print(f'#{t} {calculate(postfix)}')
