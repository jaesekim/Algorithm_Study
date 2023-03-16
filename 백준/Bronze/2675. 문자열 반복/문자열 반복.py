T = int(input())
for _ in range(T):
    times, chars = input().split()
    answer = ''
    for char in chars:
        answer += char * int(times)
    print(answer)