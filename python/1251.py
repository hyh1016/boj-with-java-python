word = input()
length = len(word)
candidate = []
for i in range(length - 2):
    for j in range(i + 1, length - 1):
        first = word[:i + 1]
        second = word[i + 1:j + 1]
        third = word[j + 1:]
        new_word = first[::-1] + second[::-1] + third[::-1]
        candidate.append(new_word)
print(sorted(candidate)[0])
