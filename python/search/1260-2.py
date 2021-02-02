# DFS/BFS
from sys import stdin
from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in range(len(graph[v])):
        if graph[v][i] == 1 and not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in range(len(graph[v])):
            if graph[v][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, start = map(int, stdin.readline().split())
graph = [[0] * (n + 1) for i in range(n + 1)]
for i in range(m):
    n1, n2 = map(int, stdin.readline().split())
    graph[n1][n2] = graph[n2][n1] = 1
dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)

dfs(graph, start, dfs_visited)
print()
bfs(graph, start, bfs_visited)
print()
