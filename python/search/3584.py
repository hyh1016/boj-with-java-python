import sys
input = sys.stdin.readline


def get_ancestors(parent, v, ancestors):
    if parent[v] == -1:
        return
    ancestors.append(parent[v])
    get_ancestors(parent, parent[v], ancestors)


for i in range(int(input())):
    n = int(input())
    parent = [-1] * (n+1)
    parent[0] = None
    for i in range(n-1):
        a, b = map(int, input().split())
        parent[b] = a
    root = parent.index(-1)
    n1, n2 = map(int, input().split())
    n1_ancestors, n2_ancestors = [n1], [n2]
    get_ancestors(parent, n1, n1_ancestors)
    get_ancestors(parent, n2, n2_ancestors)
    common_ancestors = set(n1_ancestors) & set(n2_ancestors)
    for i in n1_ancestors:
        if i in common_ancestors:
            print(i)
            break
