def inorder(node):
    if node:  # node가 있다면(0이 아니라면)
        inorder(int(tree[node][2]))  # left
        char.append(tree[node][1])
        inorder(int(tree[node][3]))  # right

for test_no in range(1, 11):
    N = int(input())
    tree = [input().split() for _ in range(N)]
    for route in tree:
        while len(route) != 4:  # 0으로 다 채워주기
            route.append('0')
    # 노드 번호와 인덱스 번호 맞춰주기 위한 작업
    tree.insert(0, ['0', '0', '0', '0'])
    char = []  # 정답을 담기 위한 빈 리스트
    
    inorder(1)  # 루트 정점 번호는 항상 1
    print(f"#{test_no} {''.join(char)}")
