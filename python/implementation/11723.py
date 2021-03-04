import sys
input = sys.stdin.readline

m = int(input())
s = set()
for i in range(m):
    input_data = input().split()
    cmd = input_data[0]
    x = 0
    if cmd != 'all' and cmd != 'empty':
        x = int(input_data[1])
    if cmd == 'add':
        s.add(x)
    elif cmd == 'remove':
        if x in s:
            s.remove(x)
    elif cmd == 'check':
        print(int(x in s))
    elif cmd == 'toggle':
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    elif cmd == 'all':
        s.update(range(1, 21))
    elif cmd == 'empty':
        s.clear()
