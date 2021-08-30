import sys
import heapq
input = sys.stdin.readline


def get_min_file_sum(k, files):
    heapq.heapify(files)
    file_sum = 0
    while len(files) > 1:
        f1 = heapq.heappop(files)
        f2 = heapq.heappop(files)
        file_sum += f1+f2
        heapq.heappush(files, f1+f2)
    return file_sum


for i in range(int(input())):
    k = int(input())
    files = list(map(int, input().split()))
    print(get_min_file_sum(k, files.copy()))
