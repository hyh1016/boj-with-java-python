import sys
input = sys.stdin.readline

c, n = map(int, input().split())
data = [tuple(map(int, input().split())) for _ in range(n)]
dp = [100001] * 1001
for i in data:
    dp[i[1]] = min(dp[i[1]], i[0])
for i in range(1, c + 1):
    for j in data:
        if i > j[1]:
            dp[i] = min(dp[i], dp[i-j[1]] + j[0])
        else:
            dp[i] = min(dp[i], dp[j[1]])
print(dp[c])
