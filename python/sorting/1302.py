from sys import stdin
input = stdin.readline

n = int(input())
books = {}
for i in range(n):
    name = input().rstrip()
    if books.get(name):
        books[name] += 1
    else:
        books[name] = 1
max_selled = sorted(books.items())
max_selled = sorted(max_selled, key=lambda x: x[1], reverse=True)[0][0]
print(max_selled)
