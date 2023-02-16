import copy
import sys
input = sys.stdin.readline

N = int(input())
bar = list()
for _ in range(N):
    bar.append(int(input()))
bar = bar[::-1]
max_index = 0  # 막대 최대 높이 중 가장 앞선 인덱스를 담아줄 변수
cnt = 1        # 보이는 막대 수, 맨 앞은 무조건 보이므로
flag = 0       # 기준이 되는 인덱스
i = 1
while i < len(bar):
    if bar[i] > bar[flag]:
        cnt += 1
        flag = copy.deepcopy(i)
    i += 1
print(cnt)