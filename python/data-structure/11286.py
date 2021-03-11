import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
h = []
answer = []
for i in range(n):
    x = int(input())
    if x == 0:
        if not h:
            answer.append(0)
        else:
            answer.append(hq.heappop(h)[1])
        continue
    hq.heappush(h, (abs(x), x))
for i in answer:
    print(i)
