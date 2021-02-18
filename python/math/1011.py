def get_minimal_value(distance):
    count = 0
    value = 1
    while True:
        if distance >= 2 * value:
            distance -= 2 * value
            count += 2
            value += 1
        else:
            break
    if distance == 0:
        return count
    if distance <= value:
        return count + 1
    return count + 2


t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    print(get_minimal_value(y - x))
