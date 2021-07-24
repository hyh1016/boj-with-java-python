import sys
input = sys.stdin.readline
MAX = 10000

dp = [0]*(MAX+1)
for i in [1, 2, 3]:
    dp[i] += 1
    for j in range(i, MAX+1):
        dp[j] += dp[j-i]

for i in range(int(input())):
    print(dp[int(input())])
