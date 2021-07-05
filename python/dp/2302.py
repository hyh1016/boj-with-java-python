import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
vip = [int(input()) for i in range(m)]

dp = [0]*(n+1)
dp[0] = dp[1] = 1
for i in range(1, n+1):
    dp[i] = dp[i-1]+dp[i-2]

seat = ""
for i in range(1, n+1):
    seat += "v" if i in vip else "n"
seats = seat.split("v")

answer = 1
for i in seats:
    answer *= dp[len(i)]
print(answer)
