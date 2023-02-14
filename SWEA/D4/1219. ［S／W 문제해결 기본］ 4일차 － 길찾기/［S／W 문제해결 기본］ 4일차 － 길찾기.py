for _ in range(10):
    test_no, E = map(int, input().split())
    pair = list(map(int, input().split()))
    arr = [[0] * 100 for _ in range(100)]
    for i in range(E):
        node1, node2 = pair[i*2], pair[i*2 + 1]
        arr[node1][node2] = 1
        # i * 2와 i*2 + 1의 순서쌍
    stack = []  # stack 리스트
    visited = [0] * 100  # 0 ~ 99 까지 방문 여부 확인
    answer = 0

    # dfs 반복문
    stack.append(0)  # 출발값은 stack에 일단 넣어줘야함 중요
    while stack:
        cur = stack.pop()
        if cur == 99:
            answer = 1
            break
        if not visited[cur]:
            visited[cur] = 1
            for w in range(100):
                if arr[cur][w] == 1 and visited[w] == 0:
                    stack.append(w)
    print(f"#{test_no} {answer}")