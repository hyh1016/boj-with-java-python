from sys import stdin
import heapq
input = stdin.readline

n = int(input())
study = []
for i in range(n):
    n, s, e = map(int, input().split())
    study.append((s, e))
study.sort()

room = [study[0][1]]
for i in range(1, len(study)):
    s, e = study[i]
    if s >= room[0]:
        heapq.heappop(room)
    heapq.heappush(room, e)
print(len(room))
