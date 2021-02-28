import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[0][0] = graph[0][0]
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + graph[i][0]
for i in range(1, m):
    dp[0][i] = dp[0][i-1] + graph[0][i]
for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + graph[i][j]
print(dp[-1][-1])
