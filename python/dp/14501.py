import sys
input = sys.stdin.readline

n = int(input())
data = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]
dp = [(0, 0)]*(n+1)
for i in range(1, n+1):
    time, pay = data[i]
    end = i + time - 1
    if end > n:
        continue
    value = 0
    for j in range(i):
        if dp[j][0] < i:
            value = max(value, dp[j][1]+pay)
    if (value > dp[i][1]) or (value == dp[i][1] and end < dp[i][0]):
        dp[i] = (end, value)
print(max(p for t, p in dp))
