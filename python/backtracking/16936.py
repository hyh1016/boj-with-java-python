import sys
input = sys.stdin.readline


def get_sequence(current, sequence, numbers):
    global flag
    if flag:
        return
    numbers.remove(current)
    sequence.append(current)
    if not numbers:
        print(*sequence)
        flag = True
        return
    candidate = [current*2]
    if current % 3 == 0:
        candidate.append(current//3)
    for i in candidate:
        if i in numbers:
            get_sequence(i, sequence, numbers)
    numbers.append(sequence.pop())


n = int(input())
numbers = list(map(int, input().split()))
flag = False
for i in numbers:
    get_sequence(i, [], numbers[::])
    if flag:
        break
