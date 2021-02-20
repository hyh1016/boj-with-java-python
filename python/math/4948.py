import sys
input = sys.stdin.readline

MAX = 123456
primes = [True] * (2 * MAX + 1)
primes[0] = primes[1] = False
for i in range(2, 2 * MAX + 1):
    if not primes[i]:
        continue
    for j in range(i * 2, 2 * MAX + 1, i):
        primes[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in range(n + 1, 2 * n + 1):
        if primes[i]:
            count += 1
    print(count)
