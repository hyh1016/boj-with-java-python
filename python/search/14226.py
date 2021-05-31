import sys
from collections import deque
input = sys.stdin.readline

s = int(input())
MAX = 2*(s-1)
visited = [[False]*(MAX+1) for _ in range(MAX+1)]
q = deque([(1, 0, 0)])
while q:
    screen, board, time = q.popleft()
    if screen == s:
        print(time)
        break
    if not visited[screen-1][board]:
        visited[screen-1][board] = True
        q.append((screen-1, board, time+1))
    if screen > s:
        continue
    if 0 < screen < s and not visited[screen+board][board]:
        visited[screen+board][board] = True
        q.append((screen+board, board, time+1))
    if not visited[screen][screen]:
        visited[screen][screen] = True
        q.append((screen, screen, time+1))
