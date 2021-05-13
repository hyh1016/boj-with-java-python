import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
q = deque([(1, 0)])
visited[1] = True
count = 0
while q:
    i, d = q.popleft()
    if d >= 2:
        continue
    for v in graph[i]:
        if not visited[v]:
            visited[v] = True
            count += 1
            q.append((v, d+1))
print(count)
