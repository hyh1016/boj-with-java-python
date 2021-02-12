MAX = 11
dp = [0] * MAX
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, MAX):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

t = int(input())
for i in range(t):
    number = int(input())
    print(dp[number])
