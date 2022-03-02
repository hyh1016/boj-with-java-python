import sys

input = sys.stdin.readline


def solution(weights):
    if weights[0] > 1:
        return 1
    for i in range(1, len(weights)):
        current_sum = sum(weights[:i])
        if current_sum + 1 < weights[i]:
            return current_sum + 1
    return sum(weights) + 1


N = int(input())
weights = sorted(list(map(int, input().split())))
print(solution(weights))
