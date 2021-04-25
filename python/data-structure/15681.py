import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))


def make_tree(graph, current, parent, tree):
    for i in graph[current]:
        if i != parent:
            tree[current].append(i)
            make_tree(graph, i, current, tree)


def count_node(tree, current, size):
    for i in tree[current]:
        count_node(tree, i, size)
        size[current] += size[i]


n, r, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
tree = [[] for _ in range(n+1)]
make_tree(graph, r, -1, tree)
size = [1] * (n+1)
count_node(tree, r, size)
for i in range(q):
    u = int(input())
    print(size[u])
