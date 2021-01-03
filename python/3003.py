chess_pieces = [1, 1, 2, 2, 2, 8]
exist_pieces = list(map(int, input().split(' ')))
for i in range(6):
    if i != 5:
        print(chess_pieces[i] - exist_pieces[i], end=' ')
        continue
    print(chess_pieces[i] - exist_pieces[i], end='')