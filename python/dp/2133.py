import sys

input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)
if N > 1:
    dp[2] = 3
    for i in range(4, N + 1, 2):
        dp[i] = dp[i - 2] * 3 + 2
        j = i - 4
        while j > 0:
            dp[i] += dp[j] * 2
            j -= 2

print(dp[N])
