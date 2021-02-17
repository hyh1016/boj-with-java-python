m, n = map(int, input().split())
prime = [True] * (n + 1)
for i in range(2, n + 1):
    number = i
    if not prime[number]:
        continue
    if number >= m:
        print(number)
    while number <= n:
        prime[number] = False
        number += i
