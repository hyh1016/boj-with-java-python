import sys
from collections import deque
input = sys.stdin.readline

MAX = 100000
n, k = map(int, input().split())
dp = [-1] * (MAX+1)

q = deque()
if n == 0:
    dp[n] = 0
    q.append(n)
else:
    while n < MAX+1:
        dp[n] = 0
        q.append(n)
        n *= 2

while True:
    index = q.popleft()
    if index == k:
        print(dp[index])
        break
    cango = []
    if 0 <= index-1:
        cango.append(index-1)
    if index+1 <= MAX:
        cango.append(index+1)
    for i in cango:
        if i == 0:
            if dp[i] == -1:
                dp[i] = dp[index]+1
                q.append(i)
            continue
        while i < MAX+1:
            if dp[i] == -1:
                dp[i] = dp[index]+1
                q.append(i)
            i *= 2
