import sys
input = sys.stdin.readline

n = int(input())
square = []
i = 1
while True:
    value = i**2
    if value > n:
        break
    square.append(value)
    i += 1
dp = [4] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    for j in square:
        if j > i:
            break
        dp[i] = min(dp[i], dp[i-j]+1)
print(dp[n])
