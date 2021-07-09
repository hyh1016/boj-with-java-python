import sys
input = sys.stdin.readline


def is_include(number):
    if number < 100:
        return True
    numbers = list(map(int, str(str(number))))
    diff = set([numbers[i]-numbers[i-1] for i in range(1, len(numbers))])
    return len(diff) == 1


n = int(input())
answer = 0
for i in range(1, n+1):
    if is_include(i):
        answer += 1
print(answer)
