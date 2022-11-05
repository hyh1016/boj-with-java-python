import sys
import heapq
input = sys.stdin.readline

n = int(input())
times = []
for _ in range(n):
    s, e = map(int, input().split(' '))
    times.append((s, e))
times.sort()
rooms = [times.pop(0)[1]]
for t in times:
    if rooms[0] <= t[0]:
        heapq.heappop(rooms)
    heapq.heappush(rooms, t[1])
print(len(rooms))
