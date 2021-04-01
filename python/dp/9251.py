import sys
input = sys.stdin.readline

str1 = [0] + list(input().rstrip())
str2 = [0] + list(input().rstrip())
dp = [[0]*len(str2) for _ in range(len(str1))]
for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
print(dp[-1][-1])
