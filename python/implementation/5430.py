from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    cmd = input().rstrip()
    n = int(input())
    array = input().rstrip()
    data = deque(array[1:len(array)-1].split(',') if n > 0 else [])
    isReversed = False
    isError = False
    for j in cmd:
        if j == 'R':
            isReversed = not isReversed
        if j == 'D':
            if not data:
                isError = True
                break
            else:
                if isReversed:
                    data.pop()
                else:
                    data.popleft()
    if isError:
        print('error')
        continue
    elif isReversed:
        data.reverse()
    print('[' + ','.join(data) + ']')
