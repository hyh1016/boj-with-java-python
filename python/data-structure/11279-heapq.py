import sys
import heapq
input = sys.stdin.readline

n = int(input())
h = []
answer = []
for i in range(n):
    x = int(input())
    if x == 0:
        if not h:
            answer.append(0)
            continue
        answer.append(-heapq.heappop(h))
    else:
        heapq.heappush(h, -x)
for i in answer:
    print(i)
