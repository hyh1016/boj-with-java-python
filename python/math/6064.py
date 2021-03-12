import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    m, n, x, y = map(int, input().split())
    x_candidate = set([i for i in range(x, m*n+1, m)])
    y_candidate = set([i for i in range(y, m*n+1, n)])
    candidate = x_candidate & y_candidate
    print(min(candidate) if candidate else -1)
