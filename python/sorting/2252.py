import sys
from collections import deque

input = sys.stdin.readline


def topology_sort(graph, topology):
    sorted = []
    q = deque()
    for i in range(N):
        if topology[i] == 0:
            q.append(i)
            topology[i] -= 1
    while q:
        i = q.popleft()
        sorted.append(i + 1)
        for j in graph[i]:
            topology[j] -= 1
            if topology[j] == 0:
                q.append(j)
    return sorted


N, M = map(int, input().split())
students = [[] for _ in range(N)]
topology = [0] * N
for _ in range(M):
    big, small = map(int, input().split())
    students[big - 1].append(small - 1)
    topology[small - 1] += 1

for i in topology_sort(students, topology):
    print(i, end=" ")
print()
