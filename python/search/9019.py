import sys
from collections import deque
input = sys.stdin.readline


def calculate(value, command):
    if command == 'D':
        return (value*2) % 10000
    elif command == 'S':
        return value-1 if value > 0 else 9999
    elif command == 'L':
        left_value = value // 1000
        return (value - left_value*1000)*10 + left_value
    elif command == 'R':
        right_value = value % 10
        return right_value*1000 + value // 10


def get_commandlist(start, target):
    visited = [False] * 10000
    q = deque([(start, '')])
    visited[start] = True
    while q:
        value, cmd = q.popleft()
        if value == target:
            return cmd
        for i in ['D', 'S', 'L', 'R']:
            new_value, new_cmd = calculate(value, i), cmd + i
            if not visited[new_value]:
                q.append((new_value, new_cmd))
                visited[new_value] = True


t = int(input())
for i in range(t):
    input_data = input().split()
    A, B = int(input_data[0]), int(input_data[1])
    print(get_commandlist(A, B))
