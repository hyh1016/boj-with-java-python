from sys import stdin

case = 1
while True:
    l, p, v = map(int, stdin.readline().split())
    if l == 0:
        break
    print(f"Case {case}:", l * (v // p) + min(l, (v % p)))
    # print("Case %d:" % case, l * (v // p) + min(l, (v % p)))
    case += 1
