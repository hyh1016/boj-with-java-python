import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e8))


def get_prime(l, current):
    if l == n:
        print(current)
        return
    for i in range(10):
        new = current*10 + i
        if is_prime(new):
            get_prime(l+1, new)


def is_prime(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True


n = int(input())
for i in [2, 3, 5, 7]:
    get_prime(1, i)
