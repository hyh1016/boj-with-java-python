import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))
for i in list(permutations(data, m)):
    print(' '.join(map(str, i)))
