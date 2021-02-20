import sys
input = sys.stdin.readline


def move(fr, to):
    global count
    global log
    count += 1
    log.append((fr, to))


def hanoi(n, fr, by, to):
    if n == 1:
        move(fr, to)
    else:
        hanoi(n-1, fr, to, by)
        move(fr, to)
        hanoi(n-1, by, fr, to)


count = 0
log = []
n = int(input())
hanoi(n, 1, 2, 3)
print(count)
for i in log:
    print(i[0], i[1])
