def moving_elements(lst, visited, s_i, s_j, a_i, a_j, r, c):
    """
    :param lst:     옮길 리스트
    :param visited: 방문 리스트
    :param s_i: start i   (row)
    :param s_j: start j   (col)
    :param a_i: arrival i (row)
    :param a_j: arrival j (col)
    :return: 옮겨진 리스트, 옮긴 요소 중 가장 작은 값
    """
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    i = 0
    local_min = lst[s_i][s_j]
    x, y = s_i, s_j
    # visited[x][y] = 1
    prev = lst[x][y]
    while True:
        nx, ny = x + dx[i], y + dy[i]
        if s_i <= nx <= a_i and s_j <= ny <= a_j and not visited[nx][ny]:
            local_min = min(local_min, lst[nx][ny])
            visited[nx][ny] = 1
            cur = lst[nx][ny]
            lst[nx][ny] = prev
            prev = cur

            x, y = nx, ny  # x, y값 바꿔주기
        elif 0 <= nx < r and 0 <= ny < c and visited[nx][ny]:
            break
        else:
            i = (i + 1) % 4
    return lst, local_min


def solution(rows, columns, queries):
    """
    :param rows:    matrix row
    :param columns: matrix column
    :param queries: 회전 목록
    """
    answer = []
    num_list = [i for i in range(1, rows * columns + 1)]
    arr = []
    start = 0
    for _ in range(rows):
        arr.append(num_list[start:start+columns])
        start += columns

    for query in queries:
        query = map(lambda x: x-1, query)  # 인덱스 맞춰주기 위해 1씩 빼주기
        s_i, s_j, a_i, a_j = query
        visited = [[0] * columns for _ in range(rows)]
        arr, min_value = moving_elements(arr, visited, s_i, s_j, a_i, a_j, rows, columns)
        answer.append(min_value)
    return answer