# 나중에 다시 풀어보기
from sys import stdin

X = int(stdin.readline())
n = 1
while True:
    if X < (n + 1) * (n + 2) / 2:
        break
    n += 1
numerator, denominator = [1, n] if n % 2 else [n, 1]
remainder = X - (n * (n + 1) // 2)
if remainder != 0:
    if numerator == 1:
        numerator += remainder - 1
        denominator -= remainder - 2
    else:
        numerator -= remainder - 2
        denominator += remainder - 1
print(str(numerator) + '/' + str(denominator))
