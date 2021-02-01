from sys import stdin

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

month, day = list(map(int, stdin.readline().split()))
today = (sum(months[:month - 1]) + day - 1) % 7
print(days[today])
