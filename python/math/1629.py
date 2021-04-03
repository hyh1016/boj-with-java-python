import sys
input = sys.stdin.readline


def get_value(a, b, c):
    if b == 1:
        return a % c
    if b % 2 == 0:
        value = get_value(a, b//2, c)
        return (value**2) % c
    else:
        value = get_value(a, b//2, c)
        return ((value**2)*a) % c


a, b, c = map(int, input().split())
print(get_value(a, b, c))
