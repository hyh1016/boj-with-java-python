from sys import stdin

n = int(stdin.readline())
words = [stdin.readline().rstrip() for i in range(n)]
count_word = {}
result = 0
for word in words:
    for i in word:
        if count_word.get(i):
            count_word[i] += 1
        else:
            count_word[i] = 1
    for key in count_word.keys():
        count = count_word.get(key)
        if count > 1:
            if key * count not in word:
                break
    if key == list(count_word.keys())[-1]:
        result += 1
    count_word = {}
print(result)
