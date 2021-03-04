import sys
input = sys.stdin.readline

m = int(input())
s = [0] * 21
for i in range(m):
    input_data = input().split()
    cmd = input_data[0]
    x = 0
    if cmd != 'all' and cmd != 'empty':
        x = int(input_data[1])
    if cmd == 'add':
        s[x] = 1
    elif cmd == 'remove':
        s[x] = 0
    elif cmd == 'check':
        print(s[x])
    elif cmd == 'toggle':
        s[x] = int(not s[x])
    elif cmd == 'all':
        s = [1] * 21
    elif cmd == 'empty':
        s = [0] * 21
