cnt = int(input())

num_list = list(map(int, input().split()))
num_list.sort()
answer = 0

for idx, time in enumerate(num_list):
    answer += time * (cnt - idx)

print(answer)