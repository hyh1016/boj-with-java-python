import sys
import heapq
input = sys.stdin.readline
INF = int(1e8) + 1


def dijkstra(graph, start, shortest):
    shortest[start] = 0
    q = [(0, start)]
    while q:
        cost, end = heapq.heappop(q)
        if cost > shortest[end]:
            continue
        for e, c in graph[end]:
            new_cost = cost+c
            if new_cost < shortest[e]:
                shortest[e] = new_cost
                heapq.heappush(q, (new_cost, e))


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for i in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
start, end = map(int, input().split())
shortest = [INF] * (n+1)
dijkstra(graph, start, shortest)
print(shortest[end])
