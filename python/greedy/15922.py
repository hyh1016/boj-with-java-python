import sys
input = sys.stdin.readline

n = int(input())
answer = 0
start, end = map(int, input().split())
for _ in range(n-1):
    x, y = map(int, input().split())
    if x > end:
        answer += end-start
        start, end = x, y
        continue
    if y > end:
        end = y
answer += end-start
print(answer)
