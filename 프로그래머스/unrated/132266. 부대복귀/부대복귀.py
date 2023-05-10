from collections import deque


def solution(n, roads, sources, destination):
    """
    :param n: 총 지역 수(부대 위치 지역 포함) 1부터 n까지 지역 번호로 구분
    :param roads: 두 지역 왕복할 수 있는 길
    :param sources: 각 부대원이 위치한 서로 다른 지역
    :param destination: 부대의 지역
    :return: destination 주어졌을 때 주어진 sources 원소 순서대로 복귀할 수 있는 최단시간
    """
    answer = []
    regions = {}
    for region in range(1, n+1):
        regions[region] = []
    for road in roads:  # 길 연결해 주기
        regions[road[0]].append(road[1])
        regions[road[1]].append(road[0])
    visited = [-1] * (n + 1)
    queue = deque()
    queue.append(destination)
    visited[destination] = 0
    while queue:
        cur = queue.popleft()
        for next_node in regions[cur]:  # 갈 수 있는 곳만 탐색
            if visited[next_node] == -1:
                visited[next_node] = visited[cur] + 1
                queue.append(next_node)
    for source in sources:
        answer.append(visited[source])
    return answer