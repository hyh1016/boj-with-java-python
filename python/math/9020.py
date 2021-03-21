import sys
input = sys.stdin.readline

MAX = 10000
primes = [True]*(MAX+1)
primes[0] = primes[1] = False
for i in range(2, MAX+1):
    if not primes[i]:
        continue
    for j in range(i+i, MAX+1, i):
        primes[j] = False

t = int(input())
for i in range(t):
    n = int(input())
    left, right = (n//2, n//2) if n % 2 == 0 else (n//2, n//2+1)
    while True:
        if primes[left] and primes[right]:
            break
        left -= 1
        right += 1
    print(left, right)
