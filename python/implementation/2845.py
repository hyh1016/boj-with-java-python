person, width = list(map(int, input().split(' ')))
actual_value = person * width
estimated_values = list(map(int, input().split(' ')))

gaps = []
for value in estimated_values:
    gaps.append(value - actual_value)
print(' '.join(map(str, gaps)))
