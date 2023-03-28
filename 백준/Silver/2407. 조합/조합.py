n, m = map(int, input().split())
m = min(m, n - m)
numerator = 1
denominator = 1
for mul in range(n, n-m, -1):
    numerator *= mul

for mul in range(1, m+1):
    denominator *= mul
print(numerator // denominator)
