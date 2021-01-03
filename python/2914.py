songs, average = list(map(int, input().split(' ')))
print(songs * (average - 1) + 1)