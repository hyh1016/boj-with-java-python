import sys
from math import sqrt
input = sys.stdin.readline
INF = 100001

n = int(input())
numbers = [i*i for i in range(1, int(sqrt(n))+1)]
dp = [INF] * (n+1)
dp[0] = 0
for i in range(1, n+1):
    for j in numbers:
        if j > i:
            break
        dp[i] = min(dp[i], dp[i-j]+1)
print(dp[n])
