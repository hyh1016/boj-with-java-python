import sys
from collections import deque
input = sys.stdin.readline

data = [0] + [deque(input().rstrip()) for _ in range(4)]
m = int(input())
q = deque()
for _ in range(m):
    i, d = map(int, input().split())
    q.append((i, d))
    visited = [False]*5
    visited[i] = True
    while q:
        i, d = q.popleft()
        if i > 1 and not visited[i-1] and data[i-1][2] != data[i][6]:
            q.append((i-1, -d))
            visited[i-1] = True
        if i < 4 and not visited[i+1] and data[i+1][6] != data[i][2]:
            q.append((i+1, -d))
            visited[i+1] = True
        data[i].appendleft(data[i].pop()) if d == 1 else data[i].append(
            data[i].popleft())
result = 0
for i in range(4):
    result += (2 ** i) if data[i+1][0] == '1' else 0
print(result)
