import sys
input = sys.stdin.readline

n, m = map(int, input().split())
hash = {}
for i in range(n):
    site, password = input().split()
    hash[site] = password
for i in range(m):
    site = input().rstrip()
    print(hash[site])
