import sys
sys.setrecursionlimit(15000)
input = sys.stdin.readline


def get_result(a, b, operator):
    if operator == 0:
        return a + b
    if operator == 1:
        return a - b
    if operator == 2:
        return a * b
    if operator == 3:
        return int(a / b)


def get_optimal_number(n, result, operators):
    global max_answer, min_answer
    if n == len(numbers):
        max_answer = max(max_answer, result)
        min_answer = min(min_answer, result)
        return
    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            get_optimal_number(
                n + 1, get_result(result, numbers[n], i), operators)
            operators[i] += 1


n = int(input())
max_answer = -1e9
min_answer = 1e9
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
get_optimal_number(1, numbers[0], operators)
print(max_answer)
print(min_answer)
