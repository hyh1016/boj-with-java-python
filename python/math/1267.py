N = int(input())
call_time = list(map(int, input().split(' ')))

count_of_30 = 0
count_of_60 = 0
for time in call_time:
    count_of_30 += time // 30 + 1
    count_of_60 += time // 60 + 1

total_of_30 = count_of_30 * 10
total_of_60 = count_of_60 * 15
if total_of_30 > total_of_60:
    print('M', total_of_60)
elif total_of_30 < total_of_60:
    print('Y', total_of_30)
else:
    print('Y M', total_of_60)
