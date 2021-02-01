from sys import stdin

N = int(stdin.readline())
plug = 1
for i in range(N):
    plug += int(stdin.readline())
print(plug - N)
