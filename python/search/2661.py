import sys
input = sys.stdin.readline


def get_sequence(sequence, length):
    global answer
    if answer != -1:
        return
    if len(sequence) == length:
        answer = sequence
        return
    for i in range(1, 4):
        new_sequence = sequence + str(i)
        if is_sequence(new_sequence):
            get_sequence(new_sequence, length)


def is_sequence(sequence):
    end = len(sequence)
    for i in range(1, end//2+1):
        if sequence[end-i:end] == sequence[end-2*i:end-i]:
            return False
    return True


answer = -1
get_sequence('', int(input()))
print(answer)
