from sys import stdin
from collections import deque
input = stdin.readline


def find_parent(tree, visited, parent):
    queue = deque([1])
    visited[1] = True
    while queue:
        node = queue.popleft()
        for i in tree[node]:
            if not visited[i]:
                parent[i] = node
                queue.append(i)
                visited[i] = True


n = int(input())
tree = [[] for _ in range(n + 1)]
for i in range(n - 1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)
visited = [False] * (n + 1)
parent = [0] * (n + 1)
find_parent(tree, visited, parent)
for i in parent[2:]:
    print(i)
