def backtracking(wcount, prev, length, end_length):
    global answer
    if length == end_length:
        answer += 1
        return

    candidate = wcount.keys()
    for k in candidate:
        if wcount[k] == 0 or prev == k:
            continue

        wcount[k] -= 1
        backtracking(wcount, k, length+1, end_length)
        wcount[k] += 1


words = list(input())
wcount = dict()
for k in words:
    if k in wcount:
        wcount[k] += 1
    else:
        wcount[k] = 1

answer = 0
if len(wcount) == len(words):
    answer = 1
    for i in range(1, len(wcount)+1):
        answer *= i
else:
    answer = 0
    backtracking(wcount, None, 0, len(words))
print(answer)
