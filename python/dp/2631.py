import sys
input = sys.stdin.readline

n = int(input())
childrens = [int(input()) for _ in range(n)]
dp = [1] * n
for i in range(n):
    for j in range(i):
        if childrens[i] > childrens[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(n - max(dp))
