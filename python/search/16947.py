import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))


def get_cycle(graph, start, v, d, visited):
    global cycle
    if start == v and d > 2:
        for i in range(1, n+1):
            if visited[i]:
                cycle.add(i)
        return
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            get_cycle(graph, start, i, d+1, visited)
            visited[i] = False


def get_distance(graph, start, cycle):
    q = deque([(start, 0)])
    visited = [False]*(n+1)
    while q:
        v, d = q.popleft()
        if v in cycle:
            return d
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append((i, d+1))


n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
cycle = set()
for i in range(1, n+1):
    visited = [False]*(n+1)
    get_cycle(graph, i, i, 0, visited)
    if cycle:
        break
for i in range(1, n+1):
    print(get_distance(graph, i, cycle), end=" ")
print()
