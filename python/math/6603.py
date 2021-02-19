import sys
input = sys.stdin.readline

while True:
    input_data = input().split()
    k, numbers = int(input_data[0]), input_data[1:]
    if k == 0:
        break
    for a in range(k):
        for b in range(a + 1, k - 4):
            for c in range(b + 1, k - 3):
                for d in range(c + 1, k - 2):
                    for e in range(d + 1, k - 1):
                        for f in range(e + 1, k):
                            print(numbers[a], numbers[b], numbers[c],
                                  numbers[d], numbers[e], numbers[f])
    print()
