n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
count = 0
if n >= 1:
    dp[1] = 1
if n >= 2:
    for i in range(2, n + 1):
        dp[i] = dp[i-1] * i
    number = str(dp[n])
    for i in range(len(number) - 1, -1, -1):
        if number[i] == '0':
            count += 1
        else:
            break
print(count)
