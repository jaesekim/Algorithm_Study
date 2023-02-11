test_no = int(input())

for _ in range(test_no):
    n = int(input())
    dp = [0, 1, 2, 4]
    if n <= 3:
        print(dp[n])
    else:
        for recur in range(1, n-2):
            dp.append(dp[recur] + dp[recur+1] + dp[recur+2])
        print(dp[-1])