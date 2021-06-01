import sys
input = sys.stdin.readline


def get_second(time):
    hms = time.split(":")
    return int(hms[0])*3600 + int(hms[1])*60 + int(hms[2])


current = get_second(input())
start = get_second(input())
max_time = 24*3600
answer = (max_time-current + start) if current > start else start-current
hour = answer//3600
minute = (answer-hour*3600)//60
second = answer-hour*3600-minute*60
print(f"{hour:02d}:{minute:02d}:{second:02d}")
