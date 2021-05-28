import sys
input = sys.stdin.readline

n = int(input())
graph = [[50]*n for _ in range(n)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for m in range(n):
    for i in range(n):
        graph[i][i] = 0
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][m]+graph[m][j])

score = 50
candidate = []
for i in range(n):
    current = max(graph[i])
    if score > current:
        score = current
        candidate = [str(i+1)]
    elif score == current:
        candidate.append(str(i+1))

print(score, len(candidate))
print(' '.join(candidate))
