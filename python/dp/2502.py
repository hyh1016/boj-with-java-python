import sys
input = sys.stdin.readline

d, k = map(int, input().split())
dp = [[0]*2 for _ in range(d+1)]
dp[1][0] = dp[2][1] = 1
for i in range(3, d+1):
    for j in range(2):
        dp[i][j] = dp[i-1][j] + dp[i-2][j]
for x in range(k):
    temp = (k - x*dp[d][0])
    if temp % dp[d][1] != 0:
        continue
    y = temp // dp[d][1]
    if y < x:
        continue
    print(x)
    print(y)
    break
