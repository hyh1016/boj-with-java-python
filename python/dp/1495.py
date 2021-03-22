import sys
input = sys.stdin.readline

MAX = 100
MAX_VOLUME = 1000

n, s, m = map(int, input().split())  # 곡 개수, 시작 볼륨, 최대 볼륨
data = list(map(int, input().split()))

dp = [[False]*(MAX_VOLUME+1) for _ in range(MAX+1)]
dp[0][s] = True
for i in range(1, n+1):
    for j in range(MAX_VOLUME+1):
        if not dp[i-1][j]:
            continue
        if j-data[i-1] >= 0:
            dp[i][j-data[i-1]] = True
        if j+data[i-1] <= m:
            dp[i][j+data[i-1]] = True
answer = [i for i in range(MAX_VOLUME+1) if dp[n][i]]
if len(answer) == 0:
    print(-1)
else:
    print(answer[-1])
