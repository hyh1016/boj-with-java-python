import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * 2 for _ in range(n)]
    dp[0] = [score[0][0], score[1][0]]
    if n >= 2:
        dp[1] = [dp[0][1] + score[0][1], dp[0][0] + score[1][1]]
        for i in range(2, n):
            dp[i][0] = max(dp[i-1][1], dp[i-2][1]) + score[0][i]
            dp[i][1] = max(dp[i-1][0], dp[i-2][0]) + score[1][i]
    print(max(dp[-1]))
