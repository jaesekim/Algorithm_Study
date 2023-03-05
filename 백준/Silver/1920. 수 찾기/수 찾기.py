def searching(nbr, N):
    start = 0
    end = N - 1
    while start <= end:
        mid = (end + start) // 2
        if arr[mid] == nbr:
            return print(1)
        elif arr[mid] > nbr:
            end = mid - 1
        elif arr[mid] < nbr:
            start = mid + 1
    return print(0)


N = int(input())
arr = sorted(list(map(int, input().split())))
M = int(input())
for num in list(map(int, input().split())):
    searching(num, N)