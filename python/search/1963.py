import sys
from collections import deque
input = sys.stdin.readline
SIZE = 10000


def get_count(current, target, count, visited):
    q = deque([(current, count)])
    while q:
        current, count = q.popleft()
        if current == target:
            return count
        for i in range(4):
            for j in range(10):
                temp = str(current)
                next = int("".join(temp[:i] + str(j) + temp[i+1:]))
                if next >= 1000 and is_prime[next] and not visited[next]:
                    visited[next] = True
                    q.append((next, count+1))
    return -1


is_prime = [True] * SIZE
for i in range(2, len(is_prime)):
    if not is_prime[i]:
        continue
    for j in range(i*i, len(is_prime), i):
        is_prime[j] = False

for i in range(int(input())):
    A, B = map(int, input().split())
    answer = get_count(A, B, 0, [False]*SIZE)
    print(answer if answer != -1 else 'Impossible')
