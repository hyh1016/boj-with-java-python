from sys import stdin
from collections import deque


def bfs(array, start, visited):
    queue = deque([start])
    visited[start] = True
    count = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1
    return count


vertex = int(stdin.readline())
edge = int(stdin.readline())
graph = [[] for i in range(vertex + 1)]
visited = [False] * (vertex + 1)
for i in range(edge):
    v1, v2 = map(int, stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
print(bfs(graph, 1, visited))
