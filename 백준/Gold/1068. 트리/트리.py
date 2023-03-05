def preorder(n):
    if n != -1:
        tree[n][-1] = 0
        preorder(tree[n][1])
        preorder(tree[n][2])


N = int(input())
tree = [[0, -1, -1, 1] for _ in range(N)]
# [부모노드, 왼쪽 자식 노드, 오른쪽 자식노드, 지워짐 여부 확인], index == 현재 노드
answer = 0
for node, par in enumerate(list(map(int, input().split()))):
    tree[node][0] = par
for idx, info in enumerate(tree):
    if info[0] == -1:
        continue
    if tree[info[0]][1] == -1:  # 현재 노드 부모노드의 왼쪽 자식노드 자리가 비었다면
        tree[info[0]][1] = idx
    else:
        tree[info[0]][2] = idx
delete_node = int(input())
if tree[delete_node][0] != -1:
    preorder(delete_node)
    # 지운 노드의 부모노드로 가서 자식노드 초기화
    tree[tree[delete_node][0]][tree[tree[delete_node][0]].index(delete_node)] = -1

    for node_info in tree:
        if node_info[-1] and node_info[1] == -1 and node_info[2] == -1:
            answer += 1
print(answer)