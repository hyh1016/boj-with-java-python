import sys
input = sys.stdin.readline
MAX = 100001

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [[MAX]*(k+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = 0
for i in range(1, n+1):
    c = coins[i-1]
    for j in range(1, k+1):
        if j >= c:
            dp[i][j] = min(dp[i-1][j], dp[i][j-c]+1)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][k] if dp[n][k] != MAX else -1)
