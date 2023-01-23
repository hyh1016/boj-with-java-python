import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()
dp = [['']*(len(str2)+1) for _ in range(len(str1)+1)]

for i in range(len(str1)-1, -1, -1):
    for j in range(len(str2)-1, -1, -1):
        if str1[i] == str2[j]:
            dp[i][j] = str1[i] + dp[i+1][j+1]
        else:
            bigger = dp[i][j+1] if len(dp[i][j+1]) > len(dp[i+1][j]) else dp[i+1][j]
            dp[i][j] = bigger

print(len(dp[0][0]))
if len(dp[0][0]) > 0:
    print(dp[0][0])
