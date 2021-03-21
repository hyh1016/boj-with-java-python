import sys
from itertools import combinations
input = sys.stdin.readline

n, s = map(int, input().split())
data = list(map(int, input().split()))
count = 0
for i in range(n):
    for j in list(combinations(data, i+1)):
        if sum(j) == s:
            count += 1
print(count)
