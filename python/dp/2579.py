import sys
input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]
dp = [[0, 0] for _ in range(n)]
dp[0][0], dp[0][1] = 0, data[0]
if n >= 2:
    dp[1][0], dp[1][1] = data[0], data[0] + data[1]
if n >= 3:
    for i in range(2, n):
        dp[i][0] = dp[i-1][1]
        dp[i][1] = max(dp[i-2][1] + data[i], dp[i-2][0] + data[i-1] + data[i])
print(dp[-1][1])
