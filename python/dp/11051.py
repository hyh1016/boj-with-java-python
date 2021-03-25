import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] * (n+1)
dp[0] = dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-1]*i
print((dp[n]//(dp[n-k] * dp[k])) % 10007)
