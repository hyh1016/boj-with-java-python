import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]
parent = list(map(int, input().split()))
root = -1
for i in range(n):
    if parent[i] == -1:
        root = i
    else:
        graph[parent[i]].append(i)
deleted = int(input())
q = deque([root] if root != deleted else [])
count = 0
while q:
    v = q.popleft()
    leaf = 0
    for i in graph[v]:
        if i != deleted:
            leaf += 1
            q.append(i)
    if not leaf:
        count += 1
print(count)
