import sys
input = sys.stdin.readline

n, k = map(int, input().split())
moneys = [int(input()) for _ in range(n)]
moneys = [i for i in moneys if i <= k]
count = 0
for i in moneys[::-1]:
    count += (k // i)
    k %= i
print(count)
