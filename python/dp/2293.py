import sys
input = sys.stdin.readline

n, k = map(int, input().split())
moneys = [int(input()) for _ in range(n)]
moneys = [i for i in moneys if i <= k]
dp = [0] * (k + 1)
dp[0] = 1
for i in moneys:
    for j in range(i, k + 1):
        # i번째 코인까지 사용하여 j-i를 만드는 경우 (나를 포함) +
        # 기존 코인들을 이용하여 j를 만드는 경우 (나를 미포함)
        dp[j] = dp[j] + dp[j-i]
print(dp[k])
