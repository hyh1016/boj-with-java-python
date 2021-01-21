constructor = set()
for A in range(10):
    for B in range(10):
        for C in range(10):
            for D in range(10):
                constructor.add(1001 * A + 101 * B + 11 * C + 2 * D)

numbers = set(range(1, 10001))
for i in sorted(numbers - constructor):
    print(i)
