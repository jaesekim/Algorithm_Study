def arr_max(arr):
    result = arr[0]
    for i in arr:
        if i > result:
            result = i
    return result

T = int(input())

for no in range(1, T+1):
    stops = [0] * 1001
    for line in range(int(input())):
        bus_type, start, finish = map(int, input().split())
        if bus_type == 1:
            for idx_1 in range(start, finish+1):
                stops[idx_1] += 1
        if bus_type == 2:
            for idx_2 in range(start, finish, 2):
                stops[idx_2] += 1
            stops[finish] += 1
        if bus_type == 3:
            if not (start % 2):
                for idx_3 in range(start, finish+1):
                    if idx_3 == (start or finish):
                        stops[idx_3] += 1
                        continue
                    if not idx_3 % 4:
                        stops[idx_3] += 1
            else:
                for idx_3 in range(start, finish+1):
                    if idx_3 == (start or finish):
                        stops[idx_3] += 1
                        continue
                    if not idx_3 % 3:
                        if idx_3 % 10 != 0:
                            stops[idx_3] += 1
    print(f"#{no} {arr_max(stops)}")