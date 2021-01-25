from sys import stdin

n = int(stdin.readline())
ropes = [int(stdin.readline()) for i in range(n)]
ropes.sort()
max_weight = 0
for i in range(n):
    weight = ropes[i] * (n - i)
    if max_weight < weight:
        max_weight = weight
print(max_weight)
