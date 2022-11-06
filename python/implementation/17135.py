from collections import deque


def count_removed(graph, one, two, three, distance):
    n, m = len(graph), len(graph[0])
    removed = set()
    for i in range(n):
        target = set()
        start = n - i - 1
        for a in [one, two, three]:
            q = deque([(1, start, a)])
            while q:
                d, y, x = q.popleft()
                if graph[y][x] == 1 and (y, x) not in removed:
                    target.add((y, x))
                    break
                for dy, dx in [(0, -1), (-1, 0), (0, 1)]:
                    ny, nx = y + dy, x + dx
                    nd = d + 1
                    if 0 <= ny < n and 0 <= nx < m and nd <= distance:
                        q.append((nd, ny, nx))
        removed.update(target)
    return len(removed)


n, m, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = -1
for i in range(m):
    for j in range(i + 1, m):
        for k in range(j + 1, m):
            answer = max(answer, count_removed(graph, i, j, k, d))
print(answer)
