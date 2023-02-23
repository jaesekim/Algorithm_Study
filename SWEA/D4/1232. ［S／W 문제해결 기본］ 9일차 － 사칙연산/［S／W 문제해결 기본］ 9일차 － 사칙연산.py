def postorder(i):
    """
    후위 순회를 수행하기 위한 함수
    :param i: 정점(노드)
    :return: cal 리스트에 후위 연산 표기
    """
    if i:  # 노드가 0이 아니라면. 자식노드가 없다면 i == 0이 돼서 if문에 안 걸린다.
        postorder(int(tree[i][2]))  # left node
        postorder(int(tree[i][3]))  # right node
        cal.append(tree[i][1])
    return


for test_no in range(1, 11):

    # 정점, 노드 값 입력 받기
    N = int(input())  # 정점의 개수
    # E = V - 1         # 간선의 수
    tree = [input().split() for _ in range(N)]
    tree.insert(0, ['0', '0', '0', '0'])
    # 각 인덱스 번호 == 정점 번호
    # 정점 번호와 인덱스를 맞춰주기 위해 가짜 리스트 insert
    # [부모노드, 값, 왼쪽, 오른쪽]

    # 자식 노드 없는 노드 '0' 값 넣어주면서 길이 맞춰주기
    for point in tree:
        while len(point) != 4:
            point.append('0')

    # 이진트리 후위연산표기법으로 바꾸기
    cal = []  # 후위 연산을 위한 빈 리스트
    postorder(1)  # root 정점은 항상 1

    # 스택을 활용한 후위 연산
    stack = []
    for char in cal:
        if char.isdecimal():
            stack.append(int(char))
        else:
            x1 = stack.pop()
            x2 = stack.pop()
            if char == '+':
                stack.append(x2 + x1)
            elif char == '-':
                stack.append(x2 - x1)
            elif char == '*':
                stack.append(x2 * x1)
            elif char == '/':
                stack.append(x2 / x1)
    print(f"#{test_no} {int(stack[-1])}")