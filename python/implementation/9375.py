import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    clothes = {}
    for j in range(n):
        n, t = input().split()
        if clothes.get(t):
            clothes[t] += 1
        else:
            clothes[t] = 1
    result = 1
    for i in clothes.values():
        result *= (i+1)
    print(result-1)
