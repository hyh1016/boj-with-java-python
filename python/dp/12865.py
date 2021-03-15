import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = []
for i in range(n):
    w, v = map(int, input().split())
    if w <= k:
        data.append((w, v))
if len(data) > 0:
    dp = [[0]*(k+1) for _ in range(len(data))]
    w, v = data[0]
    for i in range(w, k+1):
        dp[0][i] = v
    for i in range(1, len(data)):
        w, v = data[i]
        for j in range(w):
            dp[i][j] = dp[i-1][j]
        for j in range(w, k+1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
    print(dp[-1][k])
else:
    print(0)
