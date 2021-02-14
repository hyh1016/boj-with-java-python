from sys import stdin
input = stdin.readline

MAX = 101
dp = [0] * MAX

dp[1] = dp[2] = dp[3] = 1
for i in range(3, MAX):
    dp[i] = dp[i-2] + dp[i-3]

t = int(input())
for i in range(t):
    n = int(input())
    print(dp[n])
