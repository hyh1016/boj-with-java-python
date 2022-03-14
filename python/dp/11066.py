import sys

input = sys.stdin.readline
INF = int(1e10)

for i in range(int(input())):
    K = int(input())
    files = [INF] + list(map(int, input().split()))
    dp = [[INF] * (K + 1) for _ in range(K + 1)]
    files_sum = [0] * (K + 1)

    for i in range(K + 1):
        dp[i][i] = files_sum[i]

    for i in range(K + 1):
        files_sum[i] = sum(files[: i + 1])

    for i in range(1, K + 1):  # size
        for j in range(1, K - i + 1):  # start
            start, end = j, j + i
            for k in range(start, end):  # discriminator
                dp[start][end] = min(
                    dp[start][end],
                    dp[start][k]
                    + dp[k + 1][end]
                    + files_sum[end]
                    - files_sum[start - 1],
                )
    print(dp[1][K])
