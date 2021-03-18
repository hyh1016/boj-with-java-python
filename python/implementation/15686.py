import sys
from itertools import combinations
input = sys.stdin.readline


def get_distance(d1, d2):
    return abs(d1[0]-d2[0]) + abs(d1[1]-d2[1])


n, m = map(int, input().split())
houses = []
stores = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            houses.append((i, j))
        if row[j] == 2:
            stores.append((i, j))
result = 1300  # (50+50)*13
for idxs in list(combinations(range(len(stores)), m)):
    current_min = 0
    for h in houses:
        distance = 100  # 50+50
        for i in idxs:
            distance = min(distance, get_distance(h, stores[i]))
        current_min += distance
    result = min(result, current_min)
print(result)
