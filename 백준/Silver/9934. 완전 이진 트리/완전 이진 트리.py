def inorder(node):
    global index
    if node:
        inorder(tree[node][1])  # left
        tree[node][3] = route[index]
        index += 1
        inorder(tree[node][2])  # right


K = int(input())
route = list(map(int, input().split()))
node_cnt = len(route)
# [부모노드, left, right, 값], 인덱스가 노드 번호
tree = [[cur // 2, cur * 2, cur * 2 + 1, 0] for cur in range(node_cnt + 1)]
# 마지막 노드 부분 자식노드 값 0으로 넣어주기
for i in range(node_cnt, node_cnt//2, -1):
    tree[i][1] = 0
    tree[i][2] = 0
index = 0   # route 리스트를 순회할 전역변수
inorder(1)  # root는 1로 고정

# 출력
answer = []
for i in range(1, node_cnt + 1):
    answer.append(tree[i][-1])
for depth in range(K):
    print(*answer[2 ** depth - 1 : 2 ** (depth + 1) - 1])