import sys
input = sys.stdin.readline

v = {'a', 'e', 'i', 'o', 'u'}


def get_passwords(l, current, words):
    global answer
    if l == len(current):
        count_v = len(set(current) & v)
        if count_v >= 1 and l - count_v >= 2:
            answer.append(current)
        return
    for _ in range(len(words)):
        char = words.pop(0)
        get_passwords(l, current + char, words[::])


l, c = map(int, input().split())
words = sorted(list(input().split()))
answer = []
get_passwords(l, '', words)
print('\n'.join(answer))
