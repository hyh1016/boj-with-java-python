score = list(map(int, list(input())))
middle = len(score) // 2
left, right = score[:middle], score[middle:]
if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")
