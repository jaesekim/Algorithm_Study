N, K = map(int, input().split())
temperature = list(map(int, input().split()))
window = sum(temperature[:K])
max_value = window
for day in range(N - K):
    window = window - temperature[day] + temperature[day + K]
    max_value = max(max_value, window)
print(max_value)
