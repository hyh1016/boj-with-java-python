import sys
import heapq
input = sys.stdin.readline

t = int(input())
for i in range(t):
    _min = []
    _max = []
    data = {}
    k = int(input())
    for j in range(k):
        cmd, n = input().split()
        n = int(n)
        if cmd == 'I':
            heapq.heappush(_min, n)
            heapq.heappush(_max, -n)
            if n in data:
                data[n] += 1
            else:
                data[n] = 1
        elif cmd == 'D':
            if not data:
                continue
            while True:
                value = -heapq.heappop(_max) if n == 1 else heapq.heappop(_min)
                if value in data:
                    break
            if data[value] == 1:
                data.pop(value)
            else:
                data[value] -= 1
    if data:
        values = sorted(data.keys())
        print(values[-1], values[0])
    else:
        print("EMPTY")
