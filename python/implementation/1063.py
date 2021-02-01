from sys import stdin


def is_out(x, y):
    if x < 0 or x > 7 or y < 1 or y > 8:
        return True
    return False


king, stone, n = stdin.readline().split()
n = int(n)
moves = [stdin.readline().rstrip() for i in range(n)]
king_x, king_y = ord(king[0]) - ord('A'), int(king[1])
stone_x, stone_y = ord(stone[0]) - ord('A'), int(stone[1])

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]
command = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']

for i in moves:
    index = command.index(i)
    nx = king_x + dx[index]
    ny = king_y + dy[index]
    if is_out(nx, ny):
        continue
    if nx == stone_x and ny == stone_y:
        stone_nx = stone_x + dx[index]
        stone_ny = stone_y + dy[index]
        if is_out(stone_nx, stone_ny):
            continue
        stone_x, stone_y = stone_nx, stone_ny
    king_x, king_y = nx, ny

print(chr(king_x + ord('A')) + str(king_y))
print(chr(stone_x + ord('A')) + str(stone_y))
