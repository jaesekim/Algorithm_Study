T = int(input())
for test_no in range(1, T+1):
    arr = [[] for _ in range(16)]
    for _ in range(5):
        for idx, char in enumerate(list(input())):
            arr[idx].append(char)
    answer = ''
    for col in arr:
        answer += ''.join(col)
    print(f"#{test_no} {answer}")