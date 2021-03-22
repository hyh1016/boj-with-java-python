import sys
input = sys.stdin.readline
sys.setrecursionlimit(15000)


def get_max_volume(data, i, volume, visited):
    global max_volume
    if i == n:
        max_volume = max(max_volume, volume)
        return
    if volume+data[i] <= m and not visited[i][volume+data[i]]:
        visited[i][volume+data[i]] = True
        get_max_volume(data, i+1, volume+data[i], visited)
    if volume-data[i] >= 0 and not visited[i][volume-data[i]]:
        visited[i][volume-data[i]] = True
        get_max_volume(data, i+1, volume-data[i], visited)


n, s, m = map(int, input().split())  # 곡 개수, 시작 볼륨, 최대 볼륨
visited = [[False]*(m+1) for _ in range(n)]
data = list(map(int, input().split()))
max_volume = -1
get_max_volume(data, 0, s, visited)
print(max_volume)
