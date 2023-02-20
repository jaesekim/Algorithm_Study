for _ in range(1, 11):
    no = int(input())
    num_list = list(map(int, input().split()))
    subtract = 1
    while True:
        tmp = num_list[0] - subtract
        for i in range(1, 8):
            num_list[i - 1] = num_list[i]
        if tmp > 0:
            num_list[-1] = tmp
        else:
            num_list[-1] = 0
            break
        subtract += 1
        if subtract == 6:
            subtract = 1
    print(f"#{no}", *num_list)