from sys import stdin
input = stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]
dp = [0] * n
dp[0] = data[0]
if n >= 2:
    dp[1] = data[0] + data[1]
if n >= 3:
    dp[2] = sum(data[:3]) - min(data[:3])
    for i in range(3, n):
        dp[i] = max(dp[i-3] + data[i-1] + data[i], dp[i-2] + data[i], dp[i-1])
print(dp[-1])
