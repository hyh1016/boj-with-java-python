import sys
input = sys.stdin.readline

d, k = list(map(int, input().split()))

dp = [0] * d
dp[1] = dp[2] = 1
for i in range(3, d):
    dp[i] = dp[i-1]+dp[i-2]

fa = dp[d-2]
fb = dp[d-1]

for x in range(1, k):
    temp = (k - fa*x)
    if temp % fb != 0:
        continue
    y = temp // fb
    if y < x:
        continue
    print(x)
    print(y)
    break
