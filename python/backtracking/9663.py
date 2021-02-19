def dfs(n, selected):
    global answer
    current = len(selected)
    if current == n:
        answer += 1
        return
    candidate = set((range(n)))  # 선택하지 않은 열 중
    for i in range(current):  # 대각선으로 잡히는 경우 제외
        distance = current - i
        if selected[i] in candidate:
            candidate.remove(selected[i])
        if selected[i] + distance in candidate:
            candidate.remove(selected[i] + distance)
        if selected[i] - distance in candidate:
            candidate.remove(selected[i] - distance)
    for i in candidate:  # 각 후보에 대한 유망성 탐색
        dfs(n, selected[::] + [i])


n = int(input())
result = 0
for i in range(n // 2):
    answer = 0
    dfs(n, [i])
    result += (2 * answer)
if n % 2 != 0:
    answer = 0
    dfs(n, [n // 2])
    result += answer
print(result)
