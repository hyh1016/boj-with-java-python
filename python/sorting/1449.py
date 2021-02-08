from sys import stdin
input = stdin.readline

n, l = map(int, input().split())
positions = list(map(int, input().split()))
positions.sort()
prev = positions[0]
count = 1
for i in positions[1:]:
    if i < prev + l:
        continue
    prev = i
    count += 1
print(count)
