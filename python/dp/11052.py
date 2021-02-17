import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
dp = [0] + cards[::]
for i in range(2, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[j] + dp[i-j])
print(dp[n])
