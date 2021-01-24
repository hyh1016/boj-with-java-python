from sys import stdin

n, m = map(int, stdin.readline().split())  # 세로, 가로

if n == 1:
    print(1)
elif n == 2:
    print(min(4, (m - 1) // 2 + 1))
else:
    if m <= 4:
        print(m)
    elif m == 5:
        print(4)
    else:
        print(m - 2)
