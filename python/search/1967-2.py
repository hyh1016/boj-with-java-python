import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(15000)


def get_diameter(graph, v, w):
    global diameter
    candidate = []
    for i in graph[v]:
        heapq.heappush(candidate, -get_diameter(graph, i[0], i[1]))
    if len(candidate) == 0:
        return w
    else:
        first = -heapq.heappop(candidate)
        if len(candidate) > 0:
            second = -heapq.heappop(candidate)
            diameter = max(diameter, first+second)
        else:
            diameter = max(diameter, first)
        return first+w


n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    p, c, w = map(int, input().split())
    graph[p].append((c, w))
diameter = 0
get_diameter(graph, 1, 0)
print(diameter)
