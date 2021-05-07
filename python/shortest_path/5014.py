import sys
import heapq
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
shortest = [-1] * (F+1)
q = [(0, S)]
while q:
    cost, index = heapq.heappop(q)
    if shortest[index] != -1 and cost >= shortest[index]:
        continue
    shortest[index] = cost
    if index+U <= F:
        heapq.heappush(q, (cost+1, index+U))
    if index-D >= 1:
        heapq.heappush(q, (cost+1, index-D))
print(shortest[G] if shortest[G] != -1 else "use the stairs")
