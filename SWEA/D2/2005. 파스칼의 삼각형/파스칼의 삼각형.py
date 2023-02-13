T = int(input())

for test in range(1, T+1):
    N = int(input())
    pascal = [[] for _ in range(N)]
    for no in range(1, N+1):
        if no == 1:
            pascal[no-1].append(1)
        else:
            for i in range(no):
                if (i == 0) or (i == no - 1):
                    pascal[no-1].append(1)
                else:
                    pascal[no-1].append(pascal[no-2][i-1] + pascal[no-2][i])
    
    print(f"#{test}")
    for ps in pascal:
        print(*ps)