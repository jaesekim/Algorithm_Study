def bfs(start_node):
    queue = [start_node]
    # queue 담기 위한 리스트, 초기값은 출발 노드 넣어주면서 시작
    visited[start_node] = 1
    # 시작지점 방문했다고 표시
    while queue:
        cur = queue.pop(0)
        for mv in range(1, 101):
            # 현재 노드와 다음 노드가 연결돼 있고 다음 노드 방문하지 않았다면
            if contact[cur][mv] and not visited[mv]:
                queue.append(mv)
                visited[mv] = visited[cur] + 1
                # 현재 노드의 값에서 1 늘려줌으로써 몇 번째 깊이인지 표시


for test_no in range(1, 11):
    route, start = map(int, input().split())
    contact = [[0] * 101 for _ in range(101)]
    # 노드 연결을 나타내기 위한 2차원 리스트
    # 인덱스 번호와 노드 번호를 일치시키기 위해 range(101) 사용

    lst = list(map(int, input().split()))
    # contact 리스트에 연결된 노드 입력해 주기
    for i in range(0, route, 2):
        departure, arrive = lst[i], lst[i + 1]
        contact[departure][arrive] = 1

    visited = [0] * 101  # 방문한 노드를 확인하는 빈 리스트
    bfs(start)

    for node, value in enumerate(visited):
        if value == max(visited):
            answer = node
    print(f"#{test_no} {answer}")