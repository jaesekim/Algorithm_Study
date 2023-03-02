def find_last_num(nbr):
    num = 1
    compare = 0
    while True:
        compare += num
        if compare >= nbr:
            return num
        num += 1


start, finish = map(int, input().split())
series = []
last = find_last_num(finish)
n = 1
while n <= last:
    for _ in range(n):
        series.append(n)
    n += 1
print(sum(series[start-1:finish]))