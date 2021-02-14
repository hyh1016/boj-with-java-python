from sys import stdin
input = stdin.readline

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (i + 1) for i in range(n)]
dp[0][0] = triangle[0][0]
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + triangle[i][0]
    dp[i][-1] = dp[i-1][-1] + triangle[i][-1]
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
print(max(dp[-1]))
