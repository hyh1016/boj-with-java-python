name = input()
word_count = {}

for i in name:
    if word_count.get(i):
        word_count[i] += 1
    else:
        word_count[i] = 1

odd_number = 0
for i in word_count.values():
    if i % 2 != 0:
        odd_number += 1

if odd_number > 1:
    print("I'm Sorry Hansoo")
else:
    words = sorted(word_count.items())
    odd_value = None
    palindrome = ''
    for word in words:
        if word[1] % 2 != 0:
            odd_value = word[0]
            word = (word[0], word[1] - 1)
        palindrome += word[0] * (word[1] // 2)
    print(palindrome + (odd_value if odd_value else '') + palindrome[::-1])
