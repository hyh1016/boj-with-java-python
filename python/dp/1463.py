MAX = 1e6
n = int(input())
dp = [MAX] * (n + 1)
dp[0] = dp[1] = 0
for i in range(2, n + 1):
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    dp[i] = min(dp[i], dp[i-1] + 1)
print(dp[n])
