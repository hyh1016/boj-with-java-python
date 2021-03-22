import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
data = list(map(int, input().split()))
result = {}
for i in data:
    if result.get(i):
        result[i] += 1
        continue
    if len(result) == n:
        candidate = list(result.keys())
        min_key = candidate[0]
        for j in candidate:
            if result[min_key] > result[j]:
                min_key = j
        result.pop(min_key)
    result[i] = 1
print(' '.join(map(str, sorted(result.keys()))))
