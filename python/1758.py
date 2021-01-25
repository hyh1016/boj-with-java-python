from sys import stdin

n = int(stdin.readline())
tips = [int(stdin.readline()) for i in range(n)]
tips.sort(reverse=True)
total = 0
for i in range(n):
    total += max(0, tips[i] - i)
print(total)
