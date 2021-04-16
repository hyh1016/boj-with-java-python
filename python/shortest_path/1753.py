import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(graph, start, shortest):
    shortest[start] = 0
    q = [(0, start)]
    while q:
        d, v = heapq.heappop(q)
        if d > shortest[v]:
            continue
        for i in graph[v]:
            nd = d + i[1]
            if nd < shortest[i[0]]:
                shortest[i[0]] = nd
                heapq.heappush(q, (nd, i[0]))


n, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
shortest = [INF] * (n+1)
for i in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
dijkstra(graph, start, shortest)
for i in range(1, n+1):
    print(shortest[i] if shortest[i] != INF else 'INF')
