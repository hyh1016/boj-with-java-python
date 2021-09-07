from collections import deque

n = int(input())
q = deque()
count = 0
answer = -1
for i in range(10):
    count += 1
    q.append(str(i))
    if count == n:
        answer = str(i)
        q.clear()
        break
while q:
    number = q.popleft()
    for i in range(int(number[-1])):
        count += 1
        new_number = number + str(i)
        q.append(number + str(i))
        if count == n:
            answer = new_number
            break
print(answer)
