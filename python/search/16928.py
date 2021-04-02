import sys
from collections import deque
input = sys.stdin.readline


def get_optimal_value(board):
    visited = [False] * 101
    q = deque([(1, 0)])
    while q:
        v, count = q.popleft()
        if v == 100:
            return count
        for i in range(1, 7):
            nv = v+i
            if nv <= 100 and not visited[nv]:
                visited[nv] = True
                if board[nv] == 0:
                    q.append((nv, count+1))
                elif not visited[board[nv]]:
                    visited[board[nv]] = True
                    q.append((board[nv], count+1))


n, m = map(int, input().split())
board = [0] * 101
for i in range(n+m):
    x, y = map(int, input().split())
    board[x] = y
print(get_optimal_value(board))
