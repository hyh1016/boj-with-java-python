def print_score(answers):
    total_score = 0
    score = 1
    for answer in answers:
        if answer == 'O':
            total_score += score
            score += 1
        else:
            score = 1
    print(total_score)


repeat = int(input())
for i in range(repeat):
    print_score(input())
