import sys
from collections import deque
input = sys.stdin.readline


def get_sum(graph, start):
    total_sum = 0
    visited = [False] * (n + 1)
    q = deque([(start, 0)])
    visited[start] = True
    while q:
        v, d = q.popleft()
        total_sum += d
        for i in range(1, len(graph)):
            if graph[v][i] == 1 and not visited[i]:
                q.append((i, d + 1))
                visited[i] = True
    return total_sum


n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
min_result = n ** 2
min_index = 1
for i in range(1, n + 1):
    current_sum = get_sum(graph, i)
    if min_result > current_sum:
        min_result = current_sum
        min_index = i
print(min_index)
