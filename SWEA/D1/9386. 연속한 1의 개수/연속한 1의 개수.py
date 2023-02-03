T = int(input())

for no in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input()))
    count = 0
    answer = 0
    for i in range(N):
        if num_list[i] == 1:
            count += 1
            if count > answer:
                answer = count
        else:
            count = 0
    print(f"#{no} {answer}")