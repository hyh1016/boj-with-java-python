word = input().upper()
count_alphabet = [0] * 26
for i in word:
    count_alphabet[ord(i) - 65] += 1
max_alphabet_number = max(count_alphabet)
if count_alphabet.count(max_alphabet_number) == 1:
    max_alphabet_index = count_alphabet.index(max_alphabet_number)
    print(chr(max_alphabet_index + 65))
else:
    print('?')
