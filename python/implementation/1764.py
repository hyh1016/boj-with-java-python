import sys
input = sys.stdin.readline

n, m = map(int, input().split())
listen = set()
see = set()
for i in range(n):
    listen.add(input().rstrip())
for i in range(m):
    see.add(input().rstrip())
answer = sorted(listen & see)
print(len(answer))
for i in answer:
    print(i)
