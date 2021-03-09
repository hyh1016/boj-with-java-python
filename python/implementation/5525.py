import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

_next = 'I'
valid = []
count = 0
for i in range(m):
    if s[i] == _next:
        count += 1
        _next = 'I' if _next == 'O' else 'O'
    else:
        if count > 0:
            valid.append(count)
        if s[i] == 'I':
            _next = 'O'
            count = 1
        else:
            _next = 'I'
            count = 0
if count > 0:
    valid.append(count)

pn = 2 * n + 1
answer = 0
for i in valid:
    if i >= pn:
        answer += (i - pn) // 2 + 1
print(answer)
