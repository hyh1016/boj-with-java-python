import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
for i in range(n+1):
    dp[i] = dp[i-1] + data[i]
for i in range(m):
    start, end = map(int, input().split())
    print(dp[end] - dp[start-1])
