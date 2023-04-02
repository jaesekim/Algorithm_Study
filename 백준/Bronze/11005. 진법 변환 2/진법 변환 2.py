a, b = map(int, input().split())
base = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = []
while a > 0:
    answer.append(base[a % b])
    a //= b
print(''.join(answer[::-1]))