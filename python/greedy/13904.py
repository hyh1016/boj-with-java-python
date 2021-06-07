import sys
from heapq import heappush, heappop
input = sys.stdin.readline
MAX = 1000

n = int(input())
graph = [[] for _ in range(MAX+1)]
for i in range(n):
    d, w = map(int, input().split())
    heappush(graph[d], -w)
solve = []
for i in range(1, MAX+1):
    while graph[i] and len(solve) < i:
        heappush(solve, -heappop(graph[i]))
    if not solve:
        continue
    while graph[i] and solve[0] < -graph[i][0]:
        value = -heappop(graph[i])
        heappop(solve)
        heappush(solve, value)
print(sum(solve))
