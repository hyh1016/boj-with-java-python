# 2776번 집합(Set)을 이용한 풀이
t = int(input())
for i in range(t):
    n = int(input())
    note1 = set(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))
    for i in note2:
        print(1) if i in note1 else print(0)
