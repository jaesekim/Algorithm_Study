from collections import deque
import copy


def cnt_icebergs(lst):
    cnt = 0
    lst_dup = copy.deepcopy(lst)
    for i in range(N):
        for j in range(M):
            if lst_dup[i][j]:
                cnt += 1
                queue = deque()
                queue.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < M and lst_dup[nx][ny]:
                            lst_dup[nx][ny] = 0
                            queue.append((nx, ny))
    return cnt


def melting(lst, orig):
    for x in range(N):
        for y in range(M):
            cnt = 0
            if lst[x][y]:
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M and not orig[nx][ny]:
                        cnt += 1
                lst[x][y] -= cnt
                if lst[x][y] < 0:
                    lst[x][y] = 0
    return lst


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
icebergs = 1
year = 0
while icebergs == 1:
    year += 1
    original = copy.deepcopy(arr)
    arr = melting(arr, original)
    icebergs = cnt_icebergs(arr)

if icebergs >= 2:
    print(year)
else:
    print(0)

