def dfs(v, n):
    """
    :param v: 시작 정점
    :param n: 정점의 개수
    """
    visited_dfs[v] = 1
    lst_dfs.append(v)
    for w in range(1, n+1):
        if nodes[v][w] and not visited_dfs[w]:
            dfs(w, n)


def bfs(v, n):
    queue = [v]
    visited_bfs[v] = 1
    lst_bfs.append(v)
    while queue:
        cur = queue.pop(0)
        visited_bfs[cur] = 1
        for w in range(1, n+1):
            if nodes[cur][w] and not visited_bfs[w]:
                queue.append(w)
                visited_bfs[w] = 1
                lst_bfs.append(w)


N, M, V = map(int, input().split())
visited_dfs = [0] * (N + 1)
visited_bfs = [0] * (N + 1)
nodes = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    nodes[n1][n2] = 1
    nodes[n2][n1] = 1
lst_dfs = []
lst_bfs = []
dfs(V, N)
bfs(V, N)
print(*lst_dfs)
print(*lst_bfs)