n = int(input())
dp = [0] * (n + 1)
dp[1] = 3
if n >= 2:
    dp[2] = 7
    for i in range(3, n + 1):
        dp[i] = ((2 * dp[i-1]) + dp[i-2]) % 9901
print(dp[n])
