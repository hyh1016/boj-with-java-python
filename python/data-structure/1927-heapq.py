import heapq
import sys
input = sys.stdin.readline

n = int(input())
h = []
answer = []
for i in range(n):
    x = int(input())
    if x == 0:
        if len(h) == 0:
            answer.append(0)
        else:
            answer.append(heapq.heappop(h))
    else:
        heapq.heappush(h, x)
for i in answer:
    print(i)
