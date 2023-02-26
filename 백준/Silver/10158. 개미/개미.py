import copy

w, h = map(int, input().split())  # width, height
p, q = map(int, input().split())  # 시작 위치 좌표
t = int(input())                  # 계산할 시간

t_w = copy.deepcopy(t)
t_h = copy.deepcopy(t)
delta = [1, -1]
if t > 2 * w:
    t_w %= (2 * w)
if t > 2 * h:
    t_h %= (2 * h)
# x 좌표 검사
x = 0
idx_p = 0
while x < t_w:
    if 0 <= p + delta[idx_p] <= w:
        p += delta[idx_p]
        x += 1
    else:
        idx_p = (idx_p + 1) % 2

# y 좌표 검사
y = 0
idx_q = 0
while y < t_h:
    if 0 <= q + delta[idx_q] <= h:
        q += delta[idx_q]
        y += 1
    else:
        idx_q = (idx_q + 1) % 2
print(p, q, end="")