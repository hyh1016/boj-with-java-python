import sys
input = sys.stdin.readline


def get_string(candidate, count):
    result = ""
    for i in count:
        result += str(candidate.pop(i))
    return result


k = int(input())
data = input().split()
big_count = [0]*(k+1)
small_count = [0]*(k+1)
for i in range(k):
    for j in range(i, k):
        if data[j] == '>':
            break
        big_count[i] += 1
    for j in range(i, k):
        if data[j] == '<':
            break
        small_count[i] += 1
print(get_string(list(range(9, 9-k-1, -1)), big_count))
print(get_string(list(range(k+1)), small_count))
