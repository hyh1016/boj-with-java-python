import sys
input = sys.stdin.readline

lines = sorted([tuple(map(int, input().split())) for _ in range(int(input()))])

added_lines = [lines[0]]
x, y = added_lines[0]
for l in range(1, len(lines)):
    nx, ny = lines[l]
    if nx > y:
        added_lines.append((nx, ny))
        x, y = added_lines[-1]
    elif ny > y:
        added_lines[-1] = (x, ny)
        x, y = added_lines[-1]

length = 0
for x, y in added_lines:
    length += (y-x)
print(length)
